**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Verify the monitoring installation

*TODO:* run `kubectl` command to show the running pods and services for all components. Take a screenshot of the output and include it here to verify the installation
![alt text](answer-img/All_pod-service.png)

## Setup the Jaeger and Prometheus source
*TODO:* Expose Grafana to the internet and then setup Prometheus as a data source. Provide a screenshot of the home page after logging into Grafana.
![alt text](answer-img/grafana-homepage.png)
![alt text](answer-img/datasource-prometheus.png)

## Create a Basic Dashboard
*TODO:* Create a dashboard in Grafana that shows Prometheus as a source. Take a screenshot and include it here.
![alt text](answer-img/dashboard.png)

## Describe SLO/SLI
*TODO:* Describe, in your own words, what the SLIs are, based on an SLO of *monthly uptime* and *request response time*.
Monthly Uptime SLI: this measures the percentage of time the service is operational and available over a month. 
Request Response Time SLI: This measures the time taken to respond to a request. It's typically calculated as the average or percentile of response times over a given period, ensuring that the service meets the expected perfomance levels.

## Creating SLI metrics.
*TODO:* It is important to know why we want to measure certain metrics for our customer. Describe in detail 5 metrics to measure these SLIs. 

Availability: This metric tracks the percentage of time the service is up and running. It is crucial for understanding the reliability of the service and directly relates to the monthly uptime SLI.
 
Downtime Duration: Measures the total time the service is unavailable within a month. This helps identify periods of unavailability and their impact on the monthly uptime SLI.
 
Error Rate: Calculates the percentage of failed requests compared to total requests. A high error rate can affect both uptime and response time, indicating issues in service reliability.
 
Average Response Time: Measures the average time taken to respond to requests. This metric is essential for assessing the request response time SLI and ensuring the service meets performance expectations.
 
95th Percentile Response Time: Focuses on the response time for the slowest 5% of requests. This metric helps identify outliers and ensures that most requests are handled within acceptable time limits, providing a more comprehensive view of performance.

## Create a Dashboard to measure our SLIs.
*TODO:* Create a dashboard to measure the uptime of the frontend and backend services We will also want to measure to measure 40x and 50x errors. Create a dashboard that show these values over a 24 hour period and take a screenshot.
![alt text](answer-img/SLI.png)

## Tracing our Flask App
*TODO:*  We will create a Jaeger span to measure the processes on the backend. Once you fill in the span, provide a screenshot of it here. Also provide a (screenshot) sample Python file containing a trace and span code used to perform Jaeger traces on the backend service.
![alt text](answer-img/Jaeger-Backend_api.png)
![alt text](image.png)

## Jaeger in Dashboards
*TODO:* Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed, provide a screenshot of it here.
![alt text](answer-img/Jaeger-Grafana.png)

## Report Error
*TODO:* Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing (400, 500, latency) and to let them know the file that is causing the issue also include a screenshot of the tracer span to demonstrate how we can user a tracer to locate errors easily.


TROUBLE TICKET

Name: Backend "status_code 500"

Date: October 20 2024, 02:36 PM

Subject: Mogogdb operator not respond

Affected Area: Backend service

Severity: Critical
![alt text](answer-img/Jaeger_test_500_error.png)
![alt text](answer-img/Jaeger_500_error.png)


## Creating SLIs and SLOs
*TODO:* We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. Name four SLIs that you would use to measure the success of this SLO.
Availability:
Measure the percentage of time the application is accessible and operational over a given period.

Error Rate:
Track the percentage of requests that result in errors (e.g., HTTP 4xx and 5xx responses).

Response Time:
Measure the latency of key endpoints. Keeping response times within acceptable thresholds (e.g., 95th percentile) ensures a good user experience and can correlate with perceived uptime.

Service Health Checks:
Monitor the success rate of health checks for the application. This can help quickly identify issues before they impact users and overall uptime.


## Building KPIs for our plan
*TODO*: Now that we have our SLIs and SLOs, create a list of 2-3 KPIs to accurately measure these metrics as well as a description of why those KPIs were chosen. We will make a dashboard for this, but first write them down here.

Availability: The percentage of time the system is available and accessible by customers. This KPI will help us measure how often our SLIs are being met and how reliable our system is for customers.

Response Time: The amount of time it takes for the system to respond to a customer request or query. This KPI will help us measure how quickly our SLOs are being met and provide insight into user experience.

Error Rate: The percentage of requests or queries that fail or return an error code. This KPI will help us measure how often our SLIs are not being met, giving us insight into potential issues with the system that need to be addressed.

## Final Dashboard
*TODO*: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.  

![alt text](answer-img/Final_dashboard.png)
Availability: The displays the percentage of time the backend app is available 
Error Rate: This displays the number of 5xx status codes from backend
Response Time: The amount of time it takes for the system to respond to a customer request or query
