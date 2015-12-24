var chart; // global

/**
 * Request data from the server, add it to the graph and textual log and set a timeout
 * to request again - this is based on Highcharts "live data" example.
 */
function requestData() {
	$.ajax({
		url: 'get_weather_data',
		success: function(sensor_data_items) {
			var temp_series = chart.series[0],
				temp_shift = temp_series.data.length > 120; // shift if the series is
															// longer than 120 - 2 minutes worth of data

			var light_series = chart.series[1],
				light_shift = light_series.data.length > 120; // shift if the series is
															  // longer than 120 - 2 minutes worth of data
			// add the point with a timestamp
			time = (new Date()).getTime();
			temp_series.addPoint([time, sensor_data_items['data'][0]['value']], true, temp_shift);
			light_series.addPoint([time, sensor_data_items['data'][1]['value']], true, light_shift);
			
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
	Highcharts.setOptions({
		global: {
			useUTC: false
		}
	});

	chart = new Highcharts.Chart({
		chart: {
			renderTo: 'chart_container',
			defaultSeriesType: 'spline',
			marginBottom: 50,
			marginRight: 40,
			marginLeft: 40,
			marginTop: 50,
			events: {
				load: requestData
			}
		},
		title: {
			text: 'Live weather data'
		},

		tooltip: {
			shared: true,
		},

		legend: {
			y: 20,
		},

		xAxis: {
			type: 'datetime',
			tickInterval: 10 * 1e3, // ten seconds
			minorTickInterval: 5 * 1e3, // five seconds
			startOnTick: true,
			endOnTick: true,
			offset: 10,
			labels: {
				format: '{value:%H:%M:%S}'
			}
		},
		yAxis: [{ // Temperature
			title: {
				text: 'degrees Celsius',
				margin: 3,
			},
			tickInterval: 1,
			labels: {
				x: -5,
			},
		},
		{ // Light intensity
			title: {
				text: 'lux',
				margin: 3,
			},
			labels: {
				x: 5,
			},
			opposite: true,
			tickInterval: 1
		}],

		series: [{
			name: 'Temperature',
			data: []
		},
		{
			name: 'Light intensity',
			data: [],
			dashStyle: 'ShortDash',
			yAxis: 1
		}]
	});
});