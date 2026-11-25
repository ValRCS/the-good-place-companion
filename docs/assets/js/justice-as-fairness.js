"use strict";
(() => {
  const values = { A: [15,30,50,100,305], B: [70,80,100,110,140], C: [60,90,120,190,290] };
  const form = document.getElementById("veil-form");
  const result = document.getElementById("veil-result");
  if (!form || !result) return;
  const compare = () => {
    const selected = form.querySelector('input[name="society"]:checked');
    if (!selected || !Object.hasOwn(values, selected.value)) return;
    const v = values[selected.value];
    const min = Math.min(...v);
    const mean = v.reduce((sum,n) => sum+n,0)/v.length;
    const explanation = selected.value === "B" ? "This is the highest minimum among the three." : selected.value === "C" ? "This is the highest mean, but the minimum is below B." : "This has the lowest minimum.";
    result.textContent = "Society " + selected.value + ": minimum " + min + ", mean " + mean + ". " + explanation;
  };
  form.addEventListener("submit", event => { event.preventDefault(); compare(); });
  form.addEventListener("change", compare);
})();
