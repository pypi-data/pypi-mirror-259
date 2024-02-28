import logging
from itertools import islice

from gc_google_services_api.bigquery import BigQueryManager

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class BigQueryExporter:
    """
    Initializes the Bigquery exporter with the given project ID and dataset ID.

    Args:
        project_id (str): The ID of the Google Cloud project.
        dataset_id (str): The ID of the BigQuery dataset.
    """

    def __init__(self, project_id, dataset_id):
        self.project_id = project_id
        self.dataset_id = dataset_id
        self.client = BigQueryManager(
            project_id=project_id, dataset_id=dataset_id
        )
        self.batch_size = 200
        self.schemas = {
            "all_opportunity": {
                "opportunity_id": "STRING",
                "account_billing_country": "STRING",
                "account_owner": "STRING",
                "account_id": "STRING",
                "amount": "STRING",
                "amount_eur": "STRING",
                "campaign_id": "STRING",
                "close_month_formula": "STRING",
                "close_date": "STRING",
                "contact_id": "STRING",
                "curreny_iso_code": "STRING",
                "end_date": "STRING",
                "expected_revenue": "STRING",
                "fiscal": "STRING",
                "fiscal_quarter": "STRING",
                "fiscal_year": "STRING",
                "jira_default_name": "STRING",
                "ga_client_id": "STRING",
                "ga_track_id": "STRING",
                "ga_user_id": "STRING",
                "is_global": "BOOLEAN",
                "has_proposal": "BOOLEAN",
                "has_opportunity_lineitem": "BOOLEAN",
                "has_overdue_task": "BOOLEAN",
                "hasproposal": "BOOLEAN",
                "is_closed": "BOOLEAN",
                "is_won": "BOOLEAN",
                "jira_component_required": "STRING",
                "jira_estimated_work_load": "STRING",
                "jira_number": "STRING",
                "jira_work_load": "STRING",
                "jira_component_url": "STRING",
                "lead_id": "STRING",
                "lead_source": "STRING",
                "google_funding_opportunity": "STRING",
                "loss_reason": "STRING",
                "market_scope": "STRING",
                "ms_account_company_invoicing": "STRING",
                "ms_account_invoice_country_code": "STRING",
                "ms_company_origin": "STRING",
                "opportunity_name": "STRING",
                "opportunity_name_short": "STRING",
                "opportunity_requestor": "STRING",
                "owner_id": "STRING",
                "probability": "FLOAT",
                "record_type_id": "STRING",
                "roi_analysis_completed": "STRING",
                "associated_services": "STRING",
                "stage_name": "STRING",
                "tier_short": "STRING",
                "total_opportunity_quantity": "STRING",
                "start_date": "STRING",
                "year_created": "STRING",
            },
            "opportunity_line_item": {
                "opportunity_id": "STRING",
                "product_id": "STRING",
                "profit_center_name": "STRING",
                "country": "STRING",
            },
        }

        for table_name, table_schema in self.schemas.items():
            self.client.create_table_if_not_exists(table_name, table_schema)

    def _execute_query(self, query, log_id, default_error_value=None):
        custom_error_value = f"{log_id}_custom_error"

        result = self.client.execute_query(
            query,
            custom_error_value,
        )

        if result == custom_error_value:
            logging.error(
                f"[ERROR - _execute_query]: Error executing query for {log_id} in BigQuery. ({query})"  # noqa: E203
            )
            result = default_error_value

        return result

    def _export_opportunities(self, opportunities):
        opportunities_values = []
        for opp in opportunities:
            opportunities_values.append(
                f"""
                (
                    "{opp['opportunity_id']}",
                    "{opp['account_billing_country']}",
                    "{opp['account_owner']}",
                    "{opp['account_id']}",
                    "{opp['amount']}",
                    "{opp['amount_eur']}",
                    "{opp['campaign_id']}",
                    "{opp['close_month_formula']}",
                    "{opp['close_date']}",
                    "{opp['contact_id']}",
                    "{opp['curreny_iso_code']}",
                    "{opp['end_date']}",
                    "{opp['expected_revenue']}",
                    "{opp['fiscal']}",
                    "{opp['fiscal_quarter']}",
                    "{opp['fiscal_year']}",
                    "{opp['jira_default_name']}",
                    "{opp['ga_client_id']}",
                    "{opp['ga_track_id']}",
                    "{opp['ga_user_id']}",
                    {opp['is_global']},
                    {opp['has_proposal']},
                    {opp['has_opportunity_lineitem']},
                    {opp['has_overdue_task']},
                    {opp['hasproposal']},
                    {opp['is_closed']},
                    {opp['is_won']},
                    "{opp['jira_component_required']}",
                    "{opp['jira_estimated_work_load']}",
                    "{opp['jira_number']}",
                    "{opp['jira_work_load']}",
                    "{opp['jira_component_url']}",
                    "{opp['lead_id']}",
                    "{opp['lead_source']}",
                    "{opp['google_funding_opportunity']}",
                    "{opp['loss_reason']}",
                    "{opp['market_scope']}",
                    "{opp['ms_account_company_invoicing']}",
                    "{opp['ms_account_invoice_country_code']}",
                    "{opp['ms_company_origin']}",
                    "{opp['opportunity_name']}",
                    "{opp['opportunity_name_short']}",
                    "{opp['opportunity_requestor']}",
                    "{opp['owner_id']}",
                    {opp['probability']},
                    "{opp['record_type_id']}",
                    "{opp['roi_analysis_completed']}",
                    "{opp['associated_services']}",
                    "{opp['stage_name']}",
                    "{opp['tier_short']}",
                    "{opp['total_opportunity_quantity']}",
                    "{opp['start_date']}",
                    "{opp['year_created']}"
                )
                """
            )
        if opportunities_values:
            insert_opportunities_query = f"""
                INSERT INTO `{self.project_id}.{self.dataset_id}.all_opportunity` (
                    opportunity_id,
                    account_billing_country,
                    account_owner,
                    account_id,
                    amount,
                    amount_eur,
                    campaign_id,
                    close_month_formula,
                    close_date,
                    contact_id,
                    curreny_iso_code,
                    end_date,
                    expected_revenue,
                    fiscal,
                    fiscal_quarter,
                    fiscal_year,
                    jira_default_name,
                    ga_client_id,
                    ga_track_id,
                    ga_user_id,
                    is_global,
                    has_proposal,
                    has_opportunity_lineitem,
                    has_overdue_task,
                    hasproposal,
                    is_closed,
                    is_won,
                    jira_component_required,
                    jira_estimated_work_load,
                    jira_number,
                    jira_work_load,
                    jira_component_url,
                    lead_id,
                    lead_source,
                    google_funding_opportunity,
                    loss_reason,
                    market_scope,
                    ms_account_company_invoicing,
                    ms_account_invoice_country_code,
                    ms_company_origin,
                    opportunity_name,
                    opportunity_name_short,
                    opportunity_requestor,
                    owner_id,
                    probability,
                    record_type_id,
                    roi_analysis_completed,
                    associated_services,
                    stage_name,
                    tier_short,
                    total_opportunity_quantity,
                    start_date,
                    year_created
                ) VALUES {', '.join(opportunities_values)};
            """

            insert_opportunities_query = (
                insert_opportunities_query.replace("\n", "")
                .replace("    ", "")
                .replace("  ", "")
            )

            self._execute_query(
                query=insert_opportunities_query,
                log_id="INSERT_all_opportunity",
            )

    def _export_PLIs(self, opportunities):
        total_plis = sum(
            len(opp["opportunity_line_items"]) for opp in opportunities
        )

        for i in range(0, total_plis, self.batch_size):
            batch_opportunities = []
            batch_plis = []

            for opp in opportunities:
                remaining_plis = islice(
                    opp["opportunity_line_items"], i, i + self.batch_size
                )
                batch_opportunities.append(opp)
                batch_plis.extend(remaining_plis)
                opportunity_id = opp["opportunity_id"]

                if len(batch_plis) >= self.batch_size:
                    self._process_plis_batch(
                        batch_plis,
                        opportunity_id,
                    )

                    batch_opportunities = []
                    batch_plis = []

            if batch_plis:
                self._process_plis_batch(batch_plis, opportunity_id)

    def _process_plis_batch(self, plis, opportunity_id):
        plis_values = []
        for pli in plis:
            plis_values.append(
                f"""
                (
                    "{opportunity_id}",
                    "{pli['product_id']}",
                    "{pli['profit_center_name']}",
                    "{pli['country']}"
                )
                """
            )

        if plis_values:
            insert_plis_query = f"""
                INSERT INTO `{self.project_id}.{self.dataset_id}.opportunity_line_item` (
                    opportunity_id,
                    product_id,
                    profit_center_name,
                    country
                ) VALUES {', '.join(plis_values)};
            """

            insert_plis_query = (
                insert_plis_query.replace("\n", "")
                .replace("    ", "")
                .replace("  ", "")
            )

            self._execute_query(
                query=insert_plis_query,
                log_id="INSERT_opportunity_line_items",
            )

    def export_data(self, opportunities):
        opportunities_batches = [
            opportunities[i : i + self.batch_size]  # noqa: E203
            for i in range(0, len(opportunities), self.batch_size)
        ]
        for batch in opportunities_batches:
            self._export_opportunities(batch)

            self._export_PLIs(batch)

    def delete_all_rows(self):
        table_names = self.schemas.keys()
        for table_name in table_names:
            delete_query_table = f"DELETE FROM `{self.project_id}.{self.dataset_id}.{table_name}` WHERE true"  # noqa: E203
            self._execute_query(
                query=delete_query_table,
                log_id=f"delete_table_{table_name}",
            )
