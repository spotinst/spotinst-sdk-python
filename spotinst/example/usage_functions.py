import spotinst

# Initialize Spotinst Client with your Personal Access Token
client = spotinst.SpotinstClient(auth_token="YOUR_API_TOKEN_HERE")

# Initialize application
application = spotinst.spotinst_functions.Application("my_great_application")

# Create application and retrieve application-id
app = client.create_application(application)
app_id = app['id']

print "-------Create Functions Application-------"
print app_id

# Initialize providers
providers = ['aws', 'azure']

# Initialize locations
locations = ['us-east']

# Initialize environment
environment = spotinst.spotinst_functions.Environment("testings", app_id, providers, locations)

# Create environment and retrieve environment-id
env = client.create_environment(environment)
env_id = env['id']

print "-------Create Functions Environment-------"
print env_id

# Initialize function
function = spotinst.spotinst_functions.Function("ping", env_id, '/development/my_project/ping', 'main',
                                                'nodejs48', 256, 30)

# Create function and retrieve invocation URL
fx = client.create_function(function)
fx_url = fx['url']

print "-------Create Functions function-------"
print fx_url
