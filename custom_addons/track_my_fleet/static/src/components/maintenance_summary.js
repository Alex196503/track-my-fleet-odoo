/** @odoo-module **/

import { Component, useState, onWillStart } from "@odoo/owl"
import { registry } from "@web/core/registry"
import { useService } from "@web/core/utils/hooks"

export class MaintenanceSummary extends Component {
  static template = "track_my_fleet.MaintenanceSummary"
  setup() {
    this.orm = useService("orm")
    this.state = useState({
      counts: {
        needs_parts: 0,
        in_progress: 0,
        completed: 0
      },
      highPriorityList: []
    })
    onWillStart(async () => {
      await this.fetchSummaryData()
    })
  }

  async fetchSummaryData() {
    const result = await this.orm.readGroup(
      "fleet.maintenance",
      [],
      ["stage"],
      ["stage"]
    )
    const newCounts = { needs_parts: 0, in_progress: 0, completed: 0 }
    result.forEach((group) => {
      const stage = group.stage
      if (stage in newCounts && group.stage_count !== undefined) {
        newCounts[stage] = group.stage_count
      }
    })
    const highPriorityRecords = await this.orm.searchRead(
      "fleet.maintenance",
      [
        ["priority", "=", "3"],
        ["stage", "!=", "done"]
      ],
      ["id", "vehicle_id", "defect_type", "stage"]
    )
    this.state.highPriorityList = highPriorityRecords
    this.state.counts = newCounts
  }
}

registry
  .category("actions")
  .add("fleet_maintenance_summary_tag", MaintenanceSummary)
