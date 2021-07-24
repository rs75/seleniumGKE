# seleniumGKE
Simple example how to create a webcrawler with Selenium that supports javascript and deploy it to Google Compute Engine.

[app.py](app.py) contains the main application, that is automatically executed when starting the docker container.
[create_image.sh](create_image.sh) is a bash script that created the container and pushes it to the registry.
[start_vm.py](start_vm.py) is a python script to create a new VM with the previously created docker image.
Make sure to fill the placeholders in these files.

I used this architecture to create a crawler that downloads the website from various DeFi apps every day to [track the lending rates](https://investindefi.net).