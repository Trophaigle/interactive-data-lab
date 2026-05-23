const svg = d3.select("svg");

const width = 500;
const height = 300;

// échelle pour les barres
const xScale = d3.scaleBand()
  .domain(data.map(d => d.category))
  .range([0, width])
  .padding(0.3);

const yScale = d3.scaleLinear()
  .domain([0, d3.max(data, d => d.sales)])
  .range([height, 0]);

// création des barres
svg.selectAll("rect")
  .data(data)
  .enter()
  .append("rect")
  .attr("x", d => xScale(d.category))
  .attr("y", d => yScale(d.sales))
  .attr("width", xScale.bandwidth())
  .attr("height", d => height - yScale(d.sales))
  .attr("fill", "steelblue");

// labels
svg.selectAll("text")
  .data(data)
  .enter()
  .append("text")
  .attr("x", d => xScale(d.category) + 20)
  .attr("y", d => yScale(d.sales) - 5)
  .text(d => d.sales);