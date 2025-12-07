from locust import HttpUser, task, between

class PyinstrumentUser(HttpUser):
    wait_time = between(0.1, 0.3)
    
    @task
    def profile_task(self):
        self.client.get("/profile")
