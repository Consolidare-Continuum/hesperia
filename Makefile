# Hesperia repo — convenience targets (T52)
.PHONY: output-views-test
output-views-test:
	cd output_views && python3 manage.py test apps.pages
