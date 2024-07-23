-- MASTER TABLE --
CREATE TABLE Forms {
  id INTEGER,
  name TEXT NOT NULL,
  PRIMARY KEY (id)
}


-- CONSTRUCTION --
CREATE TABLE JP_541 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}


--BALANZA DE PAGOS --
CREATE TABLE JP_304 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_361 {
  id INTEGER,
  form_id INTEGER,
  income_expenses_year_1 INTEGER NOT NULL,
  income_expenses_year_2 INTEGER NOT NULL,
  income_life_1 NUMERIC NOT NULL,
  income_life_2 NUMERIC NOT NULL,
  income_disability_1 NUMERIC NOT NULL,
  income_disability_2 NUMERIC NOT NULL,
  income_auto_1 NUMERIC NOT NULL,
  income_auto_2 NUMERIC NOT NULL,
  income_other_1 NUMERIC NOT NULL,
  income_other_2 NUMERIC NOT NULL,
  income_interest_1 NUMERIC NOT NULL,
  income_interest_2 NUMERIC NOT NULL,
  income_rent_1 NUMERIC NOT NULL,
  income_rent_2 NUMERIC NOT NULL,
  income_other_2_1 NUMERIC NOT NULL,
  income_other_2_2 NUMERIC NOT NULL,
  total_income_1 NUMERIC NOT NULL,
  total_income_2 NUMERIC NOT NULL,
  expenses_life_1 NUMERIC NOT NULL,
  expenses_life_2 NUMERIC NOT NULL,
  expenses_disability_1 NUMERIC NOT NULL,
  expenses_disability_2 NUMERIC NOT NULL,
  expenses_auto_1 NUMERIC NOT NULL,
  expenses_auto_2 NUMERIC NOT NULL,
  expenses_other_1 NUMERIC NOT NULL,
  expenses_other_2 NUMERIC NOT NULL,
  expenses_salaries_1 NUMERIC NOT NULL,
  expenses_salaries_2 NUMERIC NOT NULL,
  expenses_interes_1 NUMERIC NOT NULL,
  expenses_interes_2 NUMERIC NOT NULL,
  expenses_rent_1 NUMERIC NOT NULL,
  expenses_rent_2 NUMERIC NOT NULL,
  expenses_depreciation_1 NUMERIC NOT NULL,
  expenses_depreciation_2 NUMERIC NOT NULL,
  expenses_donations_1 NUMERIC NOT NULL,
  expenses_donations_2 NUMERIC NOT NULL,
  expenses_commissions_1 NUMERIC NOT NULL,
  expenses_commissions_2 NUMERIC NOT NULL,
  expenses_employees_1 NUMERIC NOT NULL,
  expenses_employees_2 NUMERIC NOT NULL,
  expenses_brokers_1 NUMERIC NOT NULL,
  expenses_brokers_2 NUMERIC NOT NULL,
  expenses_other_operational_1 NUMERIC NOT NULL,
  expenses_other_operational_2 NUMERIC NOT NULL,
  total_expenses_1 NUMERIC NOT NULL,
  total_expenses_2 NUMERIC NOT NULL,
  net_profit_1 NUMERIC NOT NULL,
  net_profit_2 NUMERIC NOT NULL,
  balance_year_1 INTEGER NOT NULL,
  balance_year_2 INTEGER NOT NULL,
  guaranteed_1 NUMERIC NOT NULL,
  guaranteed_2 NUMERIC NOT NULL,
  guaranteed_3 NUMERIC NOT NULL,
  guaranteed_4 NUMERIC NOT NULL,
  veterans_1 NUMERIC NOT NULL,
  veterans_2 NUMERIC NOT NULL,
  veterans_3 NUMERIC NOT NULL,
  veterans_4 NUMERIC NOT NULL,
  conventional_1 NUMERIC NOT NULL,
  conventional_2 NUMERIC NOT NULL,
  conventional_3 NUMERIC NOT NULL,
  conventional_4 NUMERIC NOT NULL,
  other_1 NUMERIC NOT NULL,
  other_2 NUMERIC NOT NULL,
  other_3 NUMERIC NOT NULL,
  other_4 NUMERIC NOT NULL,
  policy_loans_1 NUMERIC NOT NULL,
  policy_loans_2 NUMERIC NOT NULL,
  policy_loans_3 NUMERIC NOT NULL,
  policy_loans_4 NUMERIC NOT NULL,
  other_specify_1 NUMERIC NOT NULL,
  other_specify_2 NUMERIC NOT NULL,
  other_specify_3 NUMERIC NOT NULL,
  other_specify_4 NUMERIC NOT NULL,
  policy_reserves_1 NUMERIC NOT NULL,
  policy_reserves_2 NUMERIC NOT NULL,
  accrued_dividends_1 NUMERIC NOT NULL,
  accrued_dividends_2 NUMERIC NOT NULL,
  signature TEXT NOT NULL,
  date TEXT NOT NULL,
  phone TEXT NOT NULL,
  position TEXT NOT NULL,

  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_362 {
  id INTEGER,
  form_id INTEGER,

  year_1 INTEGER NOT NULL,
  year_2 INTEGER NOT NULL,
  company_name TEXT NOT NULL,

  debts_balance NUMERIC NOT NULL,
  debts_emision NUMERIC NOT NULL,
  debts_amortizacion NUMERIC NOT NULL,
  debts_final NUMERIC NOT NULL,
  debts_interes NUMERIC NOT NULL,
  debts_acreedor NUMERIC NOT NULL,

  debts_bond_balance NUMERIC NOT NULL,
  debts_bond_emision NUMERIC NOT NULL,
  debts_bond_amortizacion NUMERIC NOT NULL,
  debts_bond_final NUMERIC NOT NULL,
  debts_bond_interes NUMERIC NOT NULL,
  debts_bond_acreedor NUMERIC NOT NULL,

  debts_promossory_notes_balance NUMERIC NOT NULL,
  debts_promossory_notes_emision NUMERIC NOT NULL,
  debts_promossory_notes_amortizacion NUMERIC NOT NULL,
  debts_promossory_notes_final NUMERIC NOT NULL,
  debts_promossory_notes_interes NUMERIC NOT NULL,
  debts_promossory_notes_acreedor NUMERIC NOT NULL,

  debts_others_balance NUMERIC NOT NULL,
  debts_others_emision NUMERIC NOT NULL,
  debts_others_amortizacion NUMERIC NOT NULL,
  debts_others_final NUMERIC NOT NULL,
  debts_others_interes NUMERIC NOT NULL,
  debts_others_acreedor NUMERIC NOT NULL,

  short_promossory_balance NUMERIC NOT NULL,
  short_promossory_emision NUMERIC NOT NULL,
  short_promossory_amortizacion NUMERIC NOT NULL,
  short_promossory_final NUMERIC NOT NULL,
  short_promossory_interes NUMERIC NOT NULL,
  short_promossory_acreedor NUMERIC NOT NULL,

  short_account_balance NUMERIC NOT NULL,
  short_account_emision NUMERIC NOT NULL,
  short_account_amortizacion NUMERIC NOT NULL,
  short_account_final NUMERIC NOT NULL,
  short_account_interes NUMERIC NOT NULL,
  short_account_acreedor NUMERIC NOT NULL,

  short_others_balance NUMERIC NOT NULL,
  short_others_emision NUMERIC NOT NULL,
  short_others_amortizacion NUMERIC NOT NULL,
  short_others_final NUMERIC NOT NULL,
  short_others_interes NUMERIC NOT NULL,
  short_others_acreedor NUMERIC NOT NULL,

  short_term_balance NUMERIC NOT NULL,
  short_term_emision NUMERIC NOT NULL,
  short_term_amortizacion NUMERIC NOT NULL,
  short_term_final NUMERIC NOT NULL,
  short_term_interes NUMERIC NOT NULL,
  short_term_acreedor NUMERIC NOT NULL,

  assets_balance NUMERIC NOT NULL,
  assets_emision NUMERIC NOT NULL,
  assets_amortizacion NUMERIC NOT NULL,
  assets_final NUMERIC NOT NULL,
  assets_interes NUMERIC NOT NULL,

  assets_values_balance NUMERIC NOT NULL,
  assets_values_emision NUMERIC NOT NULL,
  assets_values_amortizacion NUMERIC NOT NULL,
  assets_values_final NUMERIC NOT NULL,
  assets_values_interes NUMERIC NOT NULL,

  assets_others_balance NUMERIC NOT NULL,
  assets_others_emision NUMERIC NOT NULL,
  assets_others_amortizacion NUMERIC NOT NULL,
  assets_others_final NUMERIC NOT NULL,
  assets_others_interes NUMERIC NOT NULL,

  short_balance NUMERIC NOT NULL,
  short_emision NUMERIC NOT NULL,
  short_amortizacion NUMERIC NOT NULL,
  short_final NUMERIC NOT NULL,
  short_interes NUMERIC NOT NULL,

  short_balance_balance NUMERIC NOT NULL,
  short_balance_emision NUMERIC NOT NULL,
  short_balance_amortizacion NUMERIC NOT NULL,
  short_balance_final NUMERIC NOT NULL,
  short_balance_interes NUMERIC NOT NULL,

  short_accouts_balance NUMERIC NOT NULL,
  short_accouts_emision NUMERIC NOT NULL,
  short_accouts_amortizacion NUMERIC NOT NULL,
  short_accouts_final NUMERIC NOT NULL,
  short_accouts_interes NUMERIC NOT NULL,

  short_others_balance_2 NUMERIC NOT NULL,
  short_others_emision_2 NUMERIC NOT NULL,
  short_others_amortizacion_2 NUMERIC NOT NULL,
  short_others_final_2 NUMERIC NOT NULL,
  short_others_interes_2 NUMERIC NOT NULL,

  signature TEXT NOT NULL,
  position TEXT NOT NULL,
  date TEXT NOT NULL,
  phone TEXT NOT NULL,

  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_363 {
  id INTEGER,
  form_id INTEGER,

  bonds_year_left INTEGER NOT NULL,
  bonds_year_right INTEGER NOT NULL,
  notes_year_left INTEGER NOT NULL,
  notes_year_right INTEGER NOT NULL,

  town_bonds_left NUMERIC NOT NULL,
  town_bonds_right NUMERIC NOT NULL,
  town_notes_left NUMERIC NOT NULL,
  town_notes_right NUMERIC NOT NULL,
  town_name_service TEXT NOT NULL,

  PC_bonds_left NUMERIC NOT NULL,
  PC_bonds_right NUMERIC NOT NULL,
  PC_notes_left NUMERIC NOT NULL,
  PC_notes_right NUMERIC NOT NULL,
  PC_name_service TEXT NOT NULL,

  EPA_bonds_left NUMERIC NOT NULL,
  EPA_bonds_right NUMERIC NOT NULL,
  EPA_notes_left NUMERIC NOT NULL,
  EPA_notes_right NUMERIC NOT NULL,
  EPA_name_service TEXT NOT NULL,

  HA_bonds_left NUMERIC NOT NULL,
  HA_bonds_right NUMERIC NOT NULL,
  HA_notes_left NUMERIC NOT NULL,
  HA_notes_right NUMERIC NOT NULL,
  HA_name_service TEXT NOT NULL,

  ASA_bonds_left NUMERIC NOT NULL,
  ASA_bonds_right NUMERIC NOT NULL,
  ASA_notes_left NUMERIC NOT NULL,
  ASA_notes_right NUMERIC NOT NULL,
  ASA_name_service TEXT NOT NULL,

  PBA_bonds_left NUMERIC NOT NULL,
  PBA_bonds_right NUMERIC NOT NULL,
  PBA_notes_left NUMERIC NOT NULL,
  PBA_notes_right NUMERIC NOT NULL,
  PBA_name_service TEXT NOT NULL,

  PA_bonds_left NUMERIC NOT NULL,
  PA_bonds_right NUMERIC NOT NULL,
  PA_notes_left NUMERIC NOT NULL,
  PA_notes_right NUMERIC NOT NULL,
  PA_name_service TEXT NOT NULL,

  IDC_bonds_left NUMERIC NOT NULL,
  IDC_bonds_right NUMERIC NOT NULL,
  IDC_notes_left NUMERIC NOT NULL,
  IDC_notes_right NUMERIC NOT NULL,
  IDC_name_service TEXT NOT NULL,

  GDB_bonds_left NUMERIC NOT NULL,
  GDB_bonds_right NUMERIC NOT NULL,
  GDB_notes_left NUMERIC NOT NULL,
  GDB_notes_right NUMERIC NOT NULL,
  GDB_name_service TEXT NOT NULL,

  HFC_bonds_left NUMERIC NOT NULL,
  HFC_bonds_right NUMERIC NOT NULL,
  HFC_notes_left NUMERIC NOT NULL,
  HFC_notes_right NUMERIC NOT NULL,
  HFC_name_service TEXT NOT NULL,

  other TEXT NOT NULL,
  other_bonds_left NUMERIC NOT NULL,
  other_bonds_right NUMERIC NOT NULL,
  other_notes_left NUMERIC NOT NULL,
  other_notes_right NUMERIC NOT NULL,
  other_name_service TEXT NOT NULL,

  other_PC_1 TEXT NOT NULL,
  other_PC_1_bonds_left NUMERIC NOT NULL,
  other_PC_1_bonds_right NUMERIC NOT NULL,
  other_PC_1_notes_left NUMERIC NOT NULL,
  other_PC_1_notes_right NUMERIC NOT NULL,
  other_PC_1_name_service TEXT NOT NULL,

  other_PC_2 TEXT NOT NULL,
  other_PC_2_bonds_left NUMERIC NOT NULL,
  other_PC_2_bonds_right NUMERIC NOT NULL,
  other_PC_2_notes_left NUMERIC NOT NULL,
  other_PC_2_notes_right NUMERIC NOT NULL,
  other_PC_2_name_service TEXT NOT NULL,

  GNMA_bonds_left NUMERIC NOT NULL,
  GNMA_bonds_right NUMERIC NOT NULL,
  GNMA_notes_left NUMERIC NOT NULL,
  GNMA_notes_right NUMERIC NOT NULL,
  GNMA_name_service TEXT NOT NULL,

  other5 TEXT NOT NULL,
  other5_bonds_left NUMERIC NOT NULL,
  other5_bonds_right NUMERIC NOT NULL,
  other5_notes_left NUMERIC NOT NULL,
  other5_notes_right NUMERIC NOT NULL,
  other5_name_service TEXT NOT NULL,

  signature TEXT NOT NULL,
  position TEXT NOT NULL,
  date TEXT NOT NULL,
  phone TEXT NOT NULL,

  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_364 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_375 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_383 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_529 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_536_2 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_544 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_544_1 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_547 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}


--INGRESO NETO --
CREATE TABLE IP_110 (
  id INTEGER,
  form_id INTEGER,
  company_name TEXT NOT NULL,
  address TEXT NOT NULL,
  email TEXT NOT NULL,
  liaison_officer TEXT NOT NULL,
  ssn TEXT NOT NULL,
  tel TEXT NOT NULL,
  fax TEXT,
  legal_form TEXT NOT NULL,
  cfc TEXT NOT NULL,
  business_type TEXT NOT NULL,
  business_function TEXT NOT NULL,
  branches TEXT NOT NULL,
  closing_date TEXT NOT NULL,
  start_year INTEGER NOT NULL,
  end_year INTEGER NOT NULL,
  incomes_services_revenues_1 NUMERIC NOT NULL,
  incomes_services_revenues_2 NUMERIC NOT NULL,
  incomes_industries_1 NUMERIC NOT NULL,
  incomes_industries_2 NUMERIC NOT NULL,
  incomes_persons_1 NUMERIC NOT NULL,
  incomes_persons_2 NUMERIC NOT NULL,
  incomes_sale_merchandise_1 NUMERIC NOT NULL,
  incomes_sale_merchandise_2 NUMERIC NOT NULL,
  incomes_rents_1 NUMERIC NOT NULL,
  incomes_rents_2 NUMERIC NOT NULL,
  incomes_interests_1 NUMERIC NOT NULL,
  incomes_interests_2 NUMERIC NOT NULL,
  incomes_capital_gain_loss_1 NUMERIC NOT NULL,
  others_incomes_1 NUMERIC NOT NULL,
  total_income_1 NUMERIC NOT NULL,
  total_income_2 NUMERIC NOT NULL,
  expenses_1 NUMERIC NOT NULL,
  expenses_2 NUMERIC NOT NULL,
  expenses_salaries_wages_bonus_1 NUMERIC NOT NULL,
  expenses_salaries_wages_bonus_2 NUMERIC NOT NULL,
  expenses_interests_1 NUMERIC NOT NULL,
  expenses_interests_2 NUMERIC NOT NULL,
  expenses_rents_1 NUMERIC NOT NULL,
  expenses_rents_2 NUMERIC NOT NULL,
  expenses_depreciation_1 NUMERIC NOT NULL,
  expenses_depreciation_2 NUMERIC NOT NULL,
  expenses_bad_debts_1 NUMERIC NOT NULL,
  expenses_bad_debts_2 NUMERIC NOT NULL,
  expenses_donation_1 NUMERIC NOT NULL,
  expenses_donation_2 NUMERIC NOT NULL,
  expenses_sales_tax_1 NUMERIC NOT NULL,
  expenses_sales_tax_2 NUMERIC NOT NULL,
  expenses_machinery_1 NUMERIC NOT NULL,
  expenses_machinery_2 NUMERIC NOT NULL,
  other_purchases_1 NUMERIC NOT NULL,
  other_purchases_2 NUMERIC NOT NULL,
  licenses_1 NUMERIC NOT NULL,
  licenses_2 NUMERIC NOT NULL,
  other_expenses_1 NUMERIC NOT NULL,
  other_expenses_2 NUMERIC NOT NULL,
  total_expenses_1 NUMERIC NOT NULL,
  total_expenses_2 NUMERIC NOT NULL,
  net_profit_1 NUMERIC NOT NULL,
  net_profit_2 NUMERIC NOT NULL,
  net_profit_income_tax_1 NUMERIC NOT NULL,
  profit_after_tax_1 NUMERIC NOT NULL,
  profit_after_tax_2 NUMERIC NOT NULL,
  withheld_tax_1 NUMERIC NOT NULL,
  withheld_tax_2 NUMERIC NOT NULL,
  signature TEXT NOT NULL,
  rank TEXT,

  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id)
);


CREATE TABLE IP_210 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_220 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_230 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_310 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_310b {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_420 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_440 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_440g {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_480 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_480a {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_490 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_510 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_520 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_520a {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_520s {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_530 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_540 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_540J {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_540P {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_540S {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_540a {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_540v {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_610 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_620 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_710 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_720 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_810 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_560_63110 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_560_63111 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_560_63210 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_560_2 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}