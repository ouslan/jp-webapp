import React, { useState } from "react";
import "./IP_110_qtr.css"; // Ensure this file is in the same directory

const IP110Form: React.FC = () => {
  // State for form inputs
  const [formData, setFormData] = useState({
    company_name: "",
    address: "",
    email: "",
    liaison_officer: "",
    ssn: "",
    tel: "",
    fax: "",
    legal_form: "",
    cfc: "",
    business_type: "",
    business_function: "",
    branches: "",
    closing_date: "",
    start_year: "",
    end_year: "",
    incomes_services_revenues_1: "",
    incomes_services_revenues_2: "",
    incomes_industries_1: "",
    incomes_industries_2: "",
    incomes_persons_1: "",
    incomes_persons_2: "",
    incomes_sale_merchandise_1: "",
    incomes_sale_merchandise_2: "",
    incomes_rents_1: "",
    incomes_rents_2: "",
    incomes_interests_1: "",
    incomes_interests_2: "",
    incomes_capital_gain_loss_1: "",
    incomes_capital_gain_loss_2: "",
    others_incomes_1: "",
    others_incomes_2: "",
    total_income_1: "",
    total_income_2: "",
    expenses_1: "",
    expenses_2: "",
    expenses_salaries_wages_bonus_1: "",
    expenses_salaries_wages_bonus_2: "",
    expenses_interests_1: "",
    expenses_interests_2: "",
    expenses_rents_1: "",
    expenses_rents_2: "",
    expenses_depreciation_1: "",
    expenses_depreciation_2: "",
    expenses_bad_debts_1: "",
    expenses_bad_debts_2: "",
    expenses_donation_1: "",
    expenses_donation_2: "",
    expenses_sales_tax_1: "",
    expenses_sales_tax_2: "",
    expenses_machinery_1: "",
    expenses_machinery_2: "",
    other_purchases_1: "",
    other_purchases_2: "",
    licenses_1: "",
    licenses_2: "",
    other_expenses_1: "",
    other_expenses_2: "",
    total_expenses_1: "",
    total_expenses_2: "",
    net_profit_1: "",
    net_profit_2: "",
    net_profit_income_tax_1: "",
    net_profit_income_tax_2: "",
    profit_after_tax_1: "",
    profit_after_tax_2: "",
    withheld_tax_1: "",
    withheld_tax_2: "",

    signature: "",
    rank: "",
  });

  // Handle input changes
  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  // Handle form submission
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log("Form submitted:", formData);
    alert("Form successfully submitted!");
  };

  return (
    <div className="container">
      {/* Header Section */}
      <header className="header">
        <table>
          <tbody>
            <tr>
              <td id="header_left">
                IP-110<br />
                Gobierno de Puerto Rico<br />
                OFICINA DEL GOBERNADOR<br />
                Junta de Planificación<br />
                Subprograma de Análisis Económico<br />
                PO BOX 41119<br />
                SAN JUAN PR 00940-1119<br />
              </td>
              <td id="header_center">
                <img src="/images/JP_poster.jpg" alt="Logo Junta Planificación" id="header_image" />
                <br />
                AGRICULTURA, SILVICULTURA, PESCA Y CAZA<br />
                AGRICULTURE, FORESTRY, FISHING AND HUNTING
              </td>
              <td id="header_right">
                Government of Puerto Rico<br />
                OFFICE OF THE GOVERNOR<br />
                Puerto Rico Planning Board<br />
                Subprogram of Economic Analysis<br />
                PO BOX 41119<br />
                SAN JUAN PR 00940-1119<br />
                Tel. (787) 722-1970<br />
                Fax. (787) 727-8046<br />
                <a href="mailto:santiago_m@jp.pr.gov" className="custom-link">santiago_m@jp.pr.gov</a>
              </td>
            </tr>
          </tbody>
        </table>
      </header>

      {/* Main Form */}
      <main>
        <form onSubmit={handleSubmit}>
          <section className="body_header">
            <label>
              <strong>Nombre compañía / Company Name:</strong>
              <input type="text" name="company_name" value={formData.company_name} onChange={handleChange} required className="text-box space-between" />
            </label>

            <label>
              <strong>Dirección / Address:</strong>
              <input type="text" name="address" value={formData.address} onChange={handleChange} required className="text-box space-between" />
            </label>

            <label>
              <strong>Correo electrónico / Email:</strong>
              <input type="email" name="email" value={formData.email} onChange={handleChange} required className="text-box space-between" />
            </label>

            <label>
              <strong>Persona contacto / Liaison officer:</strong>
              <input type="text" name="liaison_officer" value={formData.liaison_officer} onChange={handleChange} required className="text-box space-between" />
            </label>
          </section>

          {/* Social Security and Contact */}
          <section className="first_section">
            <label>
              <strong>Número de Seguro Social / Social Security Number:</strong>
              <input type="text" name="ssn" value={formData.ssn} onChange={handleChange} required className="text-box space-between" />
            </label>

            <div className="first_div_container">
              <label>
                <strong>Tel:</strong>
                <input type="tel" name="tel" value={formData.tel} onChange={handleChange} required placeholder="123-456-7890" className="text-box space-between" />
              </label>

              <label>
                <strong>Fax:</strong>
                <input type="tel" name="fax" value={formData.fax} onChange={handleChange} placeholder="123-456-7890" className="text-box space-between" />
              </label>
            </div>
          </section>

          {/* Legal Form of Organization */}
          <section className="second_div">
            <strong>2. Forma legal de organización:</strong>
            <div id="options_container" className="second_div_container">
              {["Corporación/Corporation", "Sociedad/Partnership", "Cooperativa/Cooperativa", "Empresa Individual/Individual enterprise", "Empresa sin fines pecuniarios/Nonprofit organization"].map((option) => (
                <label key={option}>
                  <input type="radio" name="legal_form" value={option} checked={formData.legal_form === option} onChange={handleChange} />
                  {option}
                </label>
              ))}
            </div>
          </section>

          {/* DIV 3 - Controlled Foreign Corporations (CEC) */}
<div className="third_div">
  <strong>3. Corporaciones Extranjeras Controladas (CEC)/Controlled Foreign Corporations:</strong>
  <label>
    <input
      type="radio"
      name="cfc"
      value="Si"
      checked={formData.cfc === "Si"}
      onChange={handleChange}
    />
    Si
  </label>
  <label>
    <input
      type="radio"
      name="cfc"
      value="No"
      checked={formData.cfc === "No"}
      onChange={handleChange}
    />
    No
  </label>
</div>

{/* DIV 4 - Business Type */}
<div className="fourth_div">
  <strong>4. Clase de negocio / Type of business:</strong>
  <input
    className="text-box space-between"
    id="text-box-4"
    name="business_type"
    placeholder="Enter your text here..."
    value={formData.business_type}
    onChange={handleChange}
    required
  />
</div>

{/* DIV 5 - Business Function Description */}
<div className="fifth_div">
  <strong>5. Describa brevemente la función principal del negocio/Explain briefly the main function of the business activity:</strong>
  <br />
  <textarea
    className="text-box space-between"
    id="text-box-5"
    name="business_function"
    placeholder="Enter your text here..."
    value={formData.business_function}
    onChange={handleChange}
    required
  />
</div>

{/* DIV 6 - Branch Operations */}
<div className="six_div">
  <strong>6. ¿Opera sucursales esta firma? - Do you have branch operations?</strong>
  <label>
    <input
      type="radio"
      name="branches"
      value="Si"
      checked={formData.branches === "Si"}
      onChange={handleChange}
    />
    Si
  </label>
  <label>
    <input
      type="radio"
      name="branches"
      value="No"
      checked={formData.branches === "No"}
      onChange={handleChange}
    />
    No
  </label>
</div>

{/* DIV 7 - Closing Date */}
<div className="seven_div">
  <strong>7. Fecha de cierre de sus libros - Your accounting period closing date:</strong>
  <input
    type="month"
    id="date"
    name="closing_date"
    value={formData.closing_date}
    onChange={handleChange}
    required
  />
  <br />
  <br />
  &emsp;Nota: La información solicitada se refiere a las operaciones en Puerto Rico solamente - 
  The information requested refers to operations in Puerto Rico only
</div>

{/* DIV 8 - Information Request */}
<div className="eight_div">
  <strong>8. Favor de detallar la siguiente información - Please provide the following information:</strong>
</div>

{/* Income and Expenses Statement Header */}
<section>
  <div className="section_divider">
    ESTADO DE INGRESO Y GASTOS - INCOME AND EXPENSES STATEMENT
  </div>
  <div className="custom-line"></div>
</section>

{/* Divider Container */}
<section className="divider-container">
  <div className="section_divider_1" id="label">
    Partida - Item
  </div>

  <div className="section_divider_2" id="label">
    Año - Year
    <br />
    <input
      type="number"
      id="year"
      name="start_year"
      min="1000"
      max="9999"
      placeholder="year"
      value={formData.start_year}
      onChange={handleChange}
      required
    />
  </div>

  <div className="section_divider_3" id="label">
    Año - Year
    <br />
    <input
      type="number"
      id="year"
      name="end_year"
      min="1000"
      max="9999"
      placeholder="year"
      value={formData.end_year}
      onChange={handleChange}
      required
    />
  </div>
</section>

{/* SECTION A - Income */}
<section className="second_section">
  <div className="section">
    <h2>A. Ingresos - Income</h2>

    <div className="item">
      <label>1. Ingresos por servicios - Services Revenues</label>
      <input
        type="number"
        name="incomes_services_revenues_1"
        placeholder="$"
        value={formData.incomes_services_revenues_1}
        onChange={handleChange}
        required
      />
      <input
        type="number"
        name="incomes_services_revenues_2"
        placeholder="$"
        value={formData.incomes_services_revenues_2}
        onChange={handleChange}
        required
      />
    </div>

    <div className="item">
      <label>&emsp;a. A industrias y negocios - To industries and businesses</label>
      <input
        type="number"
        name="incomes_industries_1"
        placeholder="$"
        value={formData.incomes_industries_1}
        onChange={handleChange}
        required
      />
      <input
        type="number"
        name="incomes_industries_2"
        placeholder="$"
        value={formData.incomes_industries_2}
        onChange={handleChange}
        required
      />
    </div>

    <div className="item">
      <label>&emsp;b. A personas - To persons</label>
      <input
        type="number"
        name="incomes_persons_1"
        placeholder="$"
        value={formData.incomes_persons_1}
        onChange={handleChange}
        required
      />
      <input
        type="number"
        name="incomes_persons_2"
        placeholder="$"
        value={formData.incomes_persons_2}
        onChange={handleChange}
        required
      />
    </div>

    <div className="item">
      <label>2. Ventas - From sale of merchandise</label>
      <input
        type="number"
        name="incomes_sale_merchandise_1"
        placeholder="$"
        value={formData.incomes_sale_merchandise_1}
        onChange={handleChange}
        required
      />
      <input
        type="number"
        name="incomes_sale_merchandise_2"
        placeholder="$"
        value={formData.incomes_sale_merchandise_2}
        onChange={handleChange}
        required
      />
    </div>

    <div className="item">
      <label>3. Renta de terreno y edificio - Rent of land and building</label>
      <input
        type="number"
        name="incomes_rents_1"
        placeholder="$"
        value={formData.incomes_rents_1}
        onChange={handleChange}
        required
      />
      <input
        type="number"
        name="incomes_rents_2"
        placeholder="$"
        value={formData.incomes_rents_2}
        onChange={handleChange}
        required
      />
    </div>

    <div className="item">
      <label>4. Intereses - Interests</label>
      <input
        type="number"
        name="incomes_interests_1"
        placeholder="$"
        value={formData.incomes_interests_1}
        onChange={handleChange}
        required
      />
      <input
        type="number"
        name="incomes_interests_2"
        placeholder="$"
        value={formData.incomes_interests_2}
        onChange={handleChange}
        required
      />
    </div>

    <div className="item">
      <label>5. Ganancia o pérdida de capital - Capital gain or loss</label>
      <input
        type="number"
        name="incomes_capital_gain_loss_1"
        placeholder="$"
        value={formData.incomes_capital_gain_loss_1}
        onChange={handleChange}
        required
      />
      <input
        type="number"
        name="incomes_capital_gain_loss_2"
        placeholder="$"
        value={formData.incomes_capital_gain_loss_2}
        onChange={handleChange}
        required
      />
    </div>

    <div className="item">
      <label>6. Otros ingresos de operación - Other operating income</label>
      <input
        type="number"
        name="others_incomes_1"
        placeholder="$"
        value={formData.others_incomes_1}
        onChange={handleChange}
        required
      />
      <input
        type="number"
        name="others_incomes_2"
        placeholder="$"
        value={formData.others_incomes_2}
        onChange={handleChange}
        required
      />
    </div>

    <div className="item">
      <label>7. Total de ingresos - Total income</label>
      <input
        type="number"
        name="total_income_1"
        placeholder="$"
        value={formData.total_income_1}
        onChange={handleChange}
        required
      />
      <input
        type="number"
        name="total_income_2"
        placeholder="$"
        value={formData.total_income_2}
        onChange={handleChange}
        required
      />
    </div>
  </div>
</section>

{/* SECTION B - Expenses */}
<section className="section">
  <div id="title" className="item">
    <h2>B. Gastos - Expenses</h2>
    <input
      className="title-inputs"
      id="title-inputs"
      type="number"
      name="expenses_1"
      placeholder="$"
      value={formData.expenses_1}
      onChange={handleChange}
      required
    />
    <input
      id="title-inputs"
      type="number"
      name="expenses_2"
      placeholder="$"
      value={formData.expenses_2}
      onChange={handleChange}
      required
    />
  </div>

  {[
  { label: "1. Salarios, jornales, bono de Navidad y comisiones - Salaries, wages, Christmas bonus, and commissions", name: "expenses_salaries_wages_bonus" },
  { label: "2. Intereses - Interests", name: "expenses_interests" },
  { label: "3. Renta de terreno y edificio - Rent of land and building", name: "expenses_rents" },
  { label: "4. Depreciación - Depreciation", name: "expenses_depreciation" },
  { label: "5. Cuentas incobrables - Bad debts", name: "expenses_bad_debts" },
  { label: "6. Donativos - Donations", name: "expenses_donation" },
  { label: "7. Impuesto sobre la venta y uso - Sales and use tax", name: "expenses_sales_tax" },
  { label: "8. Licencias y patentes - Licenses and patents", name: "licenses" },
  { label: "9. Otros gastos de operación - Other operating expenses", name: "other_expenses" },
  { label: "10. Total de gastos - Total expenses", name: "total_expenses" },
].map(({ label, name }) => (
  <div className="item" key={name}>
    <label>{label}</label>
    <input
      type="number"
      name={`${name}_1`}
      placeholder="$"
      value={formData[`${name}_1` as keyof FormDataType] || ""}
      onChange={handleChange}
      required
    />
    <input
      type="number"
      name={`${name}_2`}
      placeholder="$"
      value={formData[`${name}_2` as keyof FormDataType] || ""}
      onChange={handleChange}
      required
    />
  </div>
))}

  <div className="item">
    <label>&emsp;a. Por Compra de maquinaria y equipo - On purchases of machinery and equipment</label>
    <input
      type="number"
      name="expenses_machinery_1"
      placeholder="$"
      value={formData.expenses_machinery_1}
      onChange={handleChange}
      required
    />
    <input
      type="number"
      name="expenses_machinery_2"
      placeholder="$"
      value={formData.expenses_machinery_2}
      onChange={handleChange}
      required
    />
  </div>

  <div className="item">
    <label>&emsp;b. Por otras compras - On other purchases</label>
    <input
      type="number"
      name="other_purchases_1"
      placeholder="$"
      value={formData.other_purchases_1}
      onChange={handleChange}
      required
    />
    <input
      type="number"
      name="other_purchases_2"
      placeholder="$"
      value={formData.other_purchases_2}
      onChange={handleChange}
      required
    />
  </div>
</section>

{/* SECTION C - Net Profit or Loss */}
<section className="section">
  <div id="title" className="item">
    <h2>C. Ganancia o pérdida neta ( + ó - ) - Net profit or loss ( + or - )</h2>
    <input
      className="title-inputs"
      id="title-inputs"
      type="number"
      name="net_profit_1"
      placeholder="$"
      value={formData.net_profit_1}
      onChange={handleChange}
      required
    />
    <input
      id="title-inputs"
      type="number"
      name="net_profit_2"
      placeholder="$"
      value={formData.net_profit_2}
      onChange={handleChange}
      required
    />
  </div>

  <div className="item">
    <label>1. Contribución sobre ingresos - Income tax</label>
    <input
      type="number"
      name="net_profit_income_tax_1"
      placeholder="$"
      value={formData.net_profit_income_tax_1}
      onChange={handleChange}
      required
    />
    <input
      type="number"
      name="net_profit_income_tax_2"
      placeholder="$"
      value={formData.net_profit_income_tax_2}
      onChange={handleChange}
      required
    />
  </div>

  <div className="item">
    <label>2. Ganancia después de contribución sobre ingresos - Profit after income tax</label>
    <input
      type="number"
      name="profit_after_tax_1"
      placeholder="$"
      value={formData.profit_after_tax_1}
      onChange={handleChange}
      required
    />
    <input
      type="number"
      name="profit_after_tax_2"
      placeholder="$"
      value={formData.profit_after_tax_2}
      onChange={handleChange}
      required
    />
  </div>
</section>

{/* SECTION D - Sales and Use Tax Withheld */}
<section className="section">
  <div id="title" className="item">
    <h2>D. Impuesto sobre ventas y uso retenido - Sales and use tax Withheld</h2>
    <input
      className="title-inputs"
      id="title-inputs"
      type="number"
      name="withheld_tax_1"
      placeholder="$"
      value={formData.withheld_tax_1}
      onChange={handleChange}
      required
    />
    <input
      id="title-inputs"
      type="number"
      name="withheld_tax_2"
      placeholder="$"
      value={formData.withheld_tax_2}
      onChange={handleChange}
      required
    />
  </div>
</section>


          {/* Accounting Closing Date */}
          <section className="seven_div">
            <label>
              <strong>Fecha de cierre de sus libros:</strong>
              <input type="month" name="closing_date" value={formData.closing_date} onChange={handleChange} required />
            </label>
          </section>

          {/* Signature */}
          <section>
            <label>
              <strong>Nombre de persona que suministra la información:</strong>
              <input type="text" name="signature" value={formData.signature} onChange={handleChange} required />
            </label>

            <label>
              <strong>Rango o posición en la empresa:</strong>
              <input type="text" name="rank" value={formData.rank} onChange={handleChange} required />
            </label>
          </section>

          {/* Submit Button */}
          <section className="submit-button-container">
            <button type="submit" className="submit-button">SUBMIT</button>
          </section>
        </form>
      </main>
    </div>
  );
};

export default IP110Form;