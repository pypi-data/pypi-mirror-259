import re
import unittest
from unittest import mock


class BigQueryExporterTestCase(unittest.TestCase):
    def setUp(self):
        self.project_id = "your-project-id"
        self.dataset_id = "your-dataset-id"

        self.opportunities = [
            {
                "account_billing_country": "Test",
                "account_id": "1011U00006UYtooABC",
                "account_owner": "<a href=/0053X00000DSJqj target=_blank>Lloyd Davies</a>",
                "amount": 12544.0,
                "amount_eur": 128.0,
                "associated_services": "Advertising - Omnichannel",
                "campaign_id": None,
                "close_date": "2024-03-31",
                "close_month_formula": "02 February",
                "contact_id": "006KX000001kcghYTb",
                "curreny_iso_code": "EUR",
                "end_date": "2025-02-28",
                "expected_revenue": 1254.4,
                "fiscal": "2024 1",
                "fiscal_quarter": 1,
                "fiscal_year": 2024,
                "ga_client_id": None,
                "ga_track_id": None,
                "ga_user_id": None,
                "google_funding_opportunity": None,
                "has_opportunity_lineitem": True,
                "has_overdue_task": False,
                "has_proposal": False,
                "hasproposal": False,
                "is_closed": False,
                "is_global": False,
                "is_won": False,
                "jira_component_required": True,
                "jira_component_url": "<a "
                "href=https://makingscience.atlassian.net/browse/ESMSTT0001-12083 "
                "target=_blank>View Jira Task</a>",
                "jira_default_name": "Betsson Group - Rizk Social and Search (NZ CA) - MS# "
                "7254",
                "jira_estimated_work_load": None,
                "jira_number": "ESMSTT0001-12083",
                "jira_work_load": None,
                "lead_id": None,
                "lead_source": "Crosselling/upselling",
                "loss_reason": None,
                "market_scope": "Canada;New Zealand",
                "ms_account_company_invoicing": "1111",
                "ms_account_invoice_country_code": "GB",
                "ms_company_origin": "Nara Media",
                "opportunity_id": "001Hn00000091GBhhy",
                "opportunity_line_items": [
                    {
                        "country": "GB",
                        "opportunity_id": "001Hn00000091GBhhy",
                        "product_id": "01h678000001Jpdfgdf",
                        "profit_center_name": "Performance | UK",
                    }
                ],
                "opportunity_name": "Betsson Group - (Rizk Social and Search (NZ CA)) AD OMN - Q1 2024",
                "opportunity_name_short": "Rizk Social and Search (NZ CA)",
                "opportunity_requestor": "test.test@makingscience.com",
                "owner_id": "0053X00000fjritfu",
                "probability": 10.0,
                "record_type_id": "0123X0000015tgpQAA",
                "roi_analysis_completed": False,
                "stage_name": "Qualification",
                "start_date": "2024-03-01",
                "tier_short": "T3",
                "total_opportunity_quantity": 98.0,
                "year_created": 2024.0,
            }
        ]

        self.mock_bigquery_manager = mock.patch(
            "gc_google_services_api.bigquery.BigQueryManager"
        ).start()
        from ..Bigquery import BigQueryExporter

        self.exporter = BigQueryExporter(self.project_id, self.dataset_id)

    def tearDown(self):
        self.mock_bigquery_manager.reset_mock()

    def test_export_opportunities(self):
        self.exporter._export_opportunities(self.opportunities)

        expected_query = """
            INSERT INTO `your-project-id.your-dataset-id.opportunity_line_item` (
                opportunity_id,
                product_id,
                profit_center_name,
                country
            ) VALUES (
                "001Hn00000091GBhhy",
                "01h678000001Jpdfgdf",
                "Performance|UK",
                "GB"
            );
        """
        execute_query_calls = self.exporter.client.execute_query.call_args_list

        expected_query_stripped = re.sub(r"\s+", "", expected_query)

        self.assertEqual(
            expected_query_stripped,
            re.sub(r"\s+", "", str(execute_query_calls[1][0][0])),
        )

    def test_export_PLIs(self):
        self.exporter._export_PLIs(self.opportunities)

        expected_query = """
            INSERT INTO `your-project-id.your-dataset-id.opportunity_line_item` (
                opportunity_id,
                product_id,
                profit_center_name,
                country
            ) VALUES (
                "001Hn00000091GBhhy",
                "01h678000001Jpdfgdf",
                "Performance|UK",
                "GB"
            );
        """

        execute_query_calls = self.exporter.client.execute_query.call_args_list
        expected_query_stripped = re.sub(r"\s+", "", expected_query)
        execute_query_stripped = re.sub(
            r"\s+", "", str(execute_query_calls[0][0][0])
        )

        self.assertEqual(execute_query_stripped, expected_query_stripped)

    @mock.patch(
        "ms_salesforce_api.salesforce.api.project.export_data.Bigquery.BigQueryManager"  # noqa: E501
    )
    def test_export_data(self, mock_bq_manager):
        mock_client = mock.Mock()
        mock_bq_manager.return_value = mock_client

        self.exporter.export_data(self.opportunities)

        expected_opportunities_query = """
            INSERT INTO `your-project-id.your-dataset-id.all_opportunity` (
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
            ) VALUES (
                "001Hn00000091GBhhy",
                "Test",
                "<ahref=/0053X00000DSJqjtarget=_blank>LloydDavies</a>",
                "1011U00006UYtooABC",
                "12544.0",
                "128.0",
                "None",
                "02February",
                "2024-03-31",
                "006KX000001kcghYTb",
                "EUR",
                "2025-02-28",
                "1254.4",
                "20241",
                "1",
                "2024",
                "BetssonGroup-RizkSocialandSearch(NZCA)-MS#7254",
                "None",
                "None",
                "None",
                False,
                False,
                True,
                False,
                False,
                False,
                False,
                "True",
                "None",
                "ESMSTT0001-12083",
                "None",
                "<ahref=https://makingscience.atlassian.net/browse/ESMSTT0001-12083target=_blank>ViewJiraTask</a>",
                "None",
                "Crosselling/upselling",
                "None",
                "None",
                "Canada;NewZealand",
                "1111",
                "GB",
                "NaraMedia",
                "BetssonGroup-(RizkSocialandSearch(NZCA))ADOMN-Q12024",
                "RizkSocialandSearch(NZCA)",
                "test.test@makingscience.com",
                "0053X00000fjritfu",
                10.0,
                "0123X0000015tgpQAA",
                "False",
                "Advertising-Omnichannel",
                "Qualification",
                "T3",
                "98.0",
                "2024-03-01",
                "2024.0"
            );
        """

        expected_PLIs_query = """
            INSERT INTO `your-project-id.your-dataset-id.opportunity_line_item` (
                opportunity_id,
                product_id,
                profit_center_name,
                country
            ) VALUES (
                "001Hn00000091GBhhy",
                "01h678000001Jpdfgdf",
                "Performance|UK",
                "GB"
            );
        """

        execute_query_calls = self.exporter.client.execute_query.call_args_list

        expected_opportunities_query_stripped = re.sub(
            r"\s+", "", expected_opportunities_query
        )

        execute_opportunities_query_stripped = re.sub(
            r"\s+", "", str(execute_query_calls[0][0][0])
        )

        expected_pli_query_stripped = re.sub(r"\s+", "", expected_PLIs_query)
        execute_pli_query_stripped = re.sub(
            r"\s+", "", str(execute_query_calls[1][0][0])
        )

        self.assertEqual(
            execute_opportunities_query_stripped,
            expected_opportunities_query_stripped,
        )

        self.assertEqual(
            execute_pli_query_stripped,
            expected_pli_query_stripped,
        )
