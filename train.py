import time
from tqdm import tqdm
import wandb
import random

wandb.init()

print("Begin Training\n")

for i in tqdm(range(10)):
   time.sleep(0.1)

   acc = i * i * 0.01
   loss = 100 - i * i 

   wandb.log({"acc": random.uniform(acc*0.9, acc*1.1) ,
       "loss": random.uniform(loss*0.8, loss * 2)})
        # "result":
        #     wandb.Html(
        #         """
        #         <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.16.0/components/prism-python.min.js"></script>
        #         <script src="https://app.wandb.ai/prism.css"></script>
        #         <div class="language-python">
# from github import Github

# # First create a Github instance:
# # using username and password
# g = Github("user", "password")

# # or using an access token
# g = Github("access_token")

# # Github Enterprise with custom hostname
# g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")

# # Then play with your Github objects:
# for repo in g.get_user().get_repos():
    # print(repo.name)
    # </div>
    # </div>
    # """
    # )})
