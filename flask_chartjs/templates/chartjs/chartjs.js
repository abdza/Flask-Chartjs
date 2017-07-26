{% if not is_chartjs_loaded() %}
<script src="{{ url_for('static',filename='js/Chart.bundle.min.js') }}"></script>
{{ set_chartjs_loaded() }}
{% endif %}
<script>
var {{ chart.title | lower | replace(' ','_') }}_chart = new Chart($('#{{ chart.title | lower | replace(' ','_') }}'), {
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
	}
});
</script>
