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
		},
		{% endfor %}
		],
	}
});
</script>
