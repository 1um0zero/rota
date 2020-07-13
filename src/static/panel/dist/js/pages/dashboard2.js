$(function () {
  'use strict';

  /* ChartJS
   * -------
   * Here we will create a few charts using ChartJS
   */

  //-----------------------
  //- MONTHLY SALES CHART -
  //-----------------------

  // Get context with jQuery - using jQuery's .get() method.
  var salesChartCanvas = $("#salesChart").get(0).getContext("2d");
  // This will get the first returned node in the jQuery collection.
  var salesChart = new Chart(salesChartCanvas);

  //var dias = 15;

  //var cadastros = [];
  //for (let i=0; i<dias; i++){
    //cadastros.push(900 + parseInt(Math.random() * 100));
  //}

  //var inscricoes = [];
  //for (let i=0; i<dias; i++){
    //inscricoes.push(700 + parseInt(Math.random() * 100));
  //}

  //var pedidos_feitos = [];
  //for (let i=0; i<dias; i++){
    //pedidos_feitos.push(250 + parseInt(Math.random() * 100));
  //}

  //var pedidos_aprovados = [];
  //for (let i=0; i<dias; i++){
    //pedidos_aprovados.push(50 + parseInt(Math.random() * 100));
  //}

  //var labels = [];
  //for (let i=1; i<=dias; i++){
    //labels.push((i < 9 ? ('0' + i) : i) + '/04');
  //}

  var alpha = 1;
  var salesChartData = {
    labels: window.chart_labels,
    datasets: [
      {
        label: "Cadastros",
        fillColor: "rgba(0, 192, 239, " + alpha + ")",
        pointColor: "rgba(0, 192, 239, " + alpha + ")",
        data: window.chart_users
      },
      {
        label: "Inscrições",
        fillColor: "rgba(221, 75, 57, " + alpha + ")",
        pointColor: "rgba(221, 75, 57, " + alpha + ")",
        data: window.chart_subscriptions
      },
      {
        label: "Pedidos feitos",
        fillColor: "rgba(243, 156, 18, " + alpha + ")",
        pointColor: "rgba(243, 156, 18, " + alpha + ")",
        data: window.chart_orders
      },
      {
        label: "Pagamentos confirmados",
        fillColor: "rgba(0, 166, 90, " + alpha + ")",
        pointColor: "rgba(0, 166, 90, " + alpha + ")",
        data: window.chart_payments
      }
    ]
  };

  var salesChartOptions = {
    //Boolean - If we should show the scale at all
    showScale: true,
    //Boolean - Whether grid lines are shown across the chart
    scaleShowGridLines: false,
    //String - Colour of the grid lines
    scaleGridLineColor: "rgba(0,0,0,.05)",
    //Number - Width of the grid lines
    scaleGridLineWidth: 1,
    //Boolean - Whether to show horizontal lines (except X axis)
    scaleShowHorizontalLines: true,
    //Boolean - Whether to show vertical lines (except Y axis)
    scaleShowVerticalLines: true,
    //Boolean - Whether the line is curved between points
    bezierCurve: true,
    //Number - Tension of the bezier curve between points
    bezierCurveTension: 0.3,
    //Boolean - Whether to show a dot for each point
    pointDot: false,
    //Number - Radius of each point dot in pixels
    pointDotRadius: 4,
    //Number - Pixel width of point dot stroke
    pointDotStrokeWidth: 1,
    //Number - amount extra to add to the radius to cater for hit detection outside the drawn point
    pointHitDetectionRadius: 20,
    //Boolean - Whether to show a stroke for datasets
    datasetStroke: true,
    //Number - Pixel width of dataset stroke
    datasetStrokeWidth: 2,
    //Boolean - Whether to fill the dataset with a color
    datasetFill: true,
    //String - A legend template
    legendTemplate: "<ul class=\"<%=name.toLowerCase()%>-legend\"><% for (var i=0; i<datasets.length; i++){%><li><span style=\"background-color:<%=datasets[i].lineColor%>\"></span><%=datasets[i].label%></li><%}%></ul>",
    //Boolean - whether to maintain the starting aspect ratio or not when responsive, if set to false, will take up entire container
    maintainAspectRatio: true,
    //Boolean - whether to make the chart responsive to window resizing
    responsive: true
  };

  //Create the line chart
  salesChart.Line(salesChartData, salesChartOptions);

  //---------------------------
  //- END MONTHLY SALES CHART -
  //---------------------------

});
