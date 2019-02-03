# Flask API Refugee Mobility
**About:**
The volume of Google searches for Facebook coming out of the Turkish Province of Balikesir is a strong predictor of refugees' Mediterranean crossings (see paper [here](https://panoskostakos.net/wp-content/uploads/2019/01/Trends.pdf)). I have been thinking for some time now about a possible application that could improve the reaction time of the  emergency response teams. Building on [Hemang Vyas’](https://github.com/vyashemang/flask-salary-predictor/) code, I’ve deployed a machine learning model using flask as an API that I think could be integrated into an inexpensive warning system. 

**Take it for a spin:**
Clone the git directory and run both $: python models.py and $: python server.py. Open a new terminal window and run the request.py file followed by the observed volume of the current Facebook searches in the Balikesir province ($: python request.py 90). The search volume can be extracted manually from Google Trends. I am sure I need to retrain the model with new data, but please read the paper in order to better understand how/what data have been used. 

**Future updates:**
Data from Google Trends can be crawled automatically, I might try to figure out how to integrate this functionality soon. But feel free to contribute. 
