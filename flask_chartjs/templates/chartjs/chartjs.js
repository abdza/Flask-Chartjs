{% if not is_chartjs_loaded() %}
<script src="{{ url_for('static',filename='js/Chart.bundle.min.js') }}"></script>
<script src="{{ url_for('static',filename='js/Chart.PieceLabel.js') }}"></script>
{{ set_chartjs_loaded() }}
{% endif %}
<script>
var {{ chart.slug }}_chart = new Chart($('#{{ chart.slug }}'), {
	type:'{{chart.type}}',
	data: {
		labels: {{chart.labels}},
		datasets:[
		{% for ds in chart.datasets %}
		{
			label: '{{ds.label}}',
			data: {{ds.data}},
			backgroundColor: {% if ds.backgroundColor is string %}"{{ds.backgroundColor}}"{% else %}["{{ ds.backgroundColor|join('","')}}"]{% endif %}
		},
		{% endfor %}
		],
	},
	{% if chart.options %}
	options: {
		{% if 'tooltip' in chart.options and chart.options.tooltip=='percent' %}
		tooltips: {
		      callbacks: {
			label: function(tooltipItem, data) {
				var dataset = data.datasets[tooltipItem.datasetIndex];
				var total = dataset.data.reduce(function(previousValue, currentValue, currentIndex, array) {
					return previousValue + currentValue;
				});
				var currentValue = dataset.data[tooltipItem.index];
				var currentLabel = data.labels[tooltipItem.index];
				var precentage = Math.floor(((currentValue/total) * 100)+0.5);         
				return currentLabel + ": " + precentage + "%";
				}
		      }
		}
		{% endif %}
	},
	{% endif %}
});
{% if chart.click %}
$('#{{chart.slug}}').on('click',function(evt){
	var activepoints = {{ chart.slug }}_chart.getElementsAtEvent(evt);
	{{chart.click}}(evt,activepoints);
});
{% endif %}
</script>
