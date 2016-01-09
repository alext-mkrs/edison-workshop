var chart; // global

var config = {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: "Temperature",
            data: [],
            fill: false,
            //borderDash: [5, 5],
            borderColor: "rgba(200,0,0,1)",
            backgroundColor: "rgba(200,0,0,1)",
            pointBorderColor: "rgba(200,0,0,1)",
            pointBackgroundColor: "rgba(200,0,0,1)",
            pointBorderWidth: 1,
            pointHoverRadius: 7,
            yAxisID: "y-axis-temp1",
        }, {
            label: "Light intensity",
            data: [],
            fill: false,
            //borderDash: [5, 5],
            borderColor: "rgba(0,0,200,1)",
            backgroundColor: "rgba(0,0,200,1)",
            pointBorderColor: "rgba(0,0,200,1)",
            pointBackgroundColor: "rgba(0,0,200,1)",
            pointBorderWidth: 1,
            pointHoverRadius: 7,
            yAxisID: "y-axis-light1",
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        tooltips: {
            mode: 'label',
            backgroundColor: "rgba(0,0,0,0.3)",
        },
        hover: {
            mode: 'label',
        },
        scales: {
            xAxes: [{
                display: true,
                scaleLabel: {
                    show: true,
                    labelString: 'Time'
                }
            }],
            yAxes: [{
                id: "y-axis-temp1",
                display: true,
                position: "left",
                type: "linear",
                scaleLabel: {
                    display: true,
                    labelString: 'degrees C'
                }
            }, {
                id: "y-axis-light1",
                display: true,
                position: "right",
                type: "linear",
                scaleLabel: {
                    display: true,
                    labelString: 'lux'
                },
                gridLines: {
                    drawOnChartArea: false, // only want the grid lines for one axis
                },
                ticks: {
                    beginAtZero: true,
                    suggestedMin: 0,
                    suggestedMax: 100,
                }
            }]
        }
    }
};

/**
 * Request data from the server, add it to the graph and set a timeout to request again
 */
function requestData() {
    // we'll display these many points - each point is taken once per second
    var NUMBER_OF_POINTS_TO_DISPLAY = 15;
    $.ajax({
        url: 'get_weather_data',
        success: function(sensor_data_items) {
            var temp_series = config.data.datasets[0],
                temp_shift = temp_series.data.length > NUMBER_OF_POINTS_TO_DISPLAY;

            var light_series = config.data.datasets[1],
                light_shift = light_series.data.length > NUMBER_OF_POINTS_TO_DISPLAY;

            var labels_series = config.data.labels,
                labels_shift = labels_series.length > NUMBER_OF_POINTS_TO_DISPLAY;

            // add the Temperature point with a timestamp
            time = new Date();
            if (temp_shift) {
                temp_series.data.shift()
            }
            temp_series.data.push(sensor_data_items['data'][0]['value']);

            // add the Light intensity point with the same timestamp
            if (light_shift) {
                light_series.data.shift()
            }
            light_series.data.push(sensor_data_items['data'][1]['value']);

            // add timestamp to Labels
            if (labels_shift) {
                labels_series.shift()
            }
            labels_series.push(time.toLocaleTimeString());

            // update chart
            chart.update()

            // Set values for our textual data representation
            for (var i=0; i < sensor_data_items['data'].length; i++) {
                var name = sensor_data_items['data'][i]['name'];
                var value = sensor_data_items['data'][i]['value'];
                var units = sensor_data_items['data'][i]['units'];
                $('#sensor_data_'+i).text(name + ': ' + value + ' ' + units);
            }

            // call it again after one second
            setTimeout(requestData, 1000);
        },
        cache: false
    });
}

$(document).ready(function() {
    console.log(config.data);

    var ctx = document.getElementById("chart_canvas").getContext("2d");
    chart = new Chart(ctx, config);

    updateLegend();
    requestData();
});

function updateLegend() {
    $legendContainer = $('#legend_container');
    $legendContainer.empty();
    $legendContainer.append(chart.generateLegend());
}