# fsr

to install - pip install fsr

to run job - fsr serve path/fileName.json -t test_type
(fsr serve report_p.json -t goldens)

<!-- logic for update py code -->

python setup.py sdist bdist_wheel
twine upload dist/\*

<!-- uninstall -->

pip uninstall fsr
pip install fsr
