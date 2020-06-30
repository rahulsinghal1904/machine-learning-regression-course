#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


import turicreate


# In[2]:


sales=turicreate.SFrame('home_data_ass1')


# In[3]:


sales


# In[4]:


train_data,test_data = sales.random_split(.8,seed=0)


# In[5]:


def simple_linear_regression(input_feature, output):
    [your code here]
return(intercept, slope)


# In[6]:


def simple_linear_regression(input_feature, output):
    Xi = input_feature
    Yi = output
    N = len(Xi)
    # compute the mean of  input_feature and output
    Ymean = Yi.mean()
    Xmean = Xi.mean()
    
    # compute the product of the output and the input_feature and its mean
    SumYiXi = (Yi * Xi).sum()
    YiXiByN = (Yi.sum() * Xi.sum()) / N
    
    # compute the squared value of the input_feature and its mean
    XiSq = (Xi * Xi).sum()
    XiXiByN = (Xi.sum() * Xi.sum()) / N
    
    # use the formula for the slope
    slope = (SumYiXi - YiXiByN) / (XiSq - XiXiByN)
    
    # use the formula for the intercept
    intercept = Ymean - (slope * Xmean)
    return (intercept, slope)


# In[7]:


test_feature = graphlab.SArray(range(5))
test_output = graphlab.SArray(1 + 1*test_feature)
(test_intercept, test_slope) =  simple_linear_regression(test_feature, test_output)
print "Intercept: " + str(test_intercept)
print "Slope: " + str(test_slope)


# In[8]:


test_feature = turicreate.SArray(range(5))
test_output = turicreate.SArray(1 + 1*test_feature)
(test_intercept, test_slope) =  simple_linear_regression(test_feature, test_output)
print "Intercept: " + str(test_intercept)
print "Slope: " + str(test_slope)


# In[9]:


test_feature = turicreate.SArray(range(5))
test_output = turicreate.SArray(1 + 1*test_feature)
(test_intercept, test_slope) =  simple_linear_regression(test_feature, test_output)
print ("Intercept: " + str(test_intercept))
print ("Slope: " + str(test_slope))


# In[10]:


sqft_intercept, sqft_slope = simple_linear_regression(train_data['sqft_living'], train_data['price'])

print ("Intercept: " + str(sqft_intercept))
print ("Slope: " + str(sqft_slope))


# In[11]:


def get_regression_predictions(input_feature, intercept, slope):
    # calculate the predicted values:
    predicted_values = intercept + (slope * input_feature)
    return predicted_values


# In[12]:


my_house_sqft = 2650
estimated_price = get_regression_predictions(my_house_sqft, sqft_intercept, sqft_slope)
print "The estimated price for a house with %d squarefeet is $%.2f" % (my_house_sqft, estimated_price)


# In[13]:


my_house_sqft = 2650
estimated_price = get_regression_predictions(my_house_sqft, sqft_intercept, sqft_slope)
print ("The estimated price for a house with %d squarefeet is $%.2f" % (my_house_sqft, estimated_price))


# In[14]:


def get_residual_sum_of_squares(input_feature, output, intercept, slope):
    # First get the predictions
    predicted_values = intercept + (slope * input_feature)
    # then compute the residuals (since we are squaring it doesn't matter which order you subtract)
    residuals = output - predicted_values
    # square the residuals and add them up
    RSS = (residuals * residuals).sum()
    return(RSS)


# In[15]:


print (get_residual_sum_of_squares(test_feature, test_output, test_intercept, test_slope)) # should be 0.0


# In[16]:


rss_prices_on_sqft = get_residual_sum_of_squares(train_data['sqft_living'], train_data['price'], sqft_intercept, sqft_slope)
print ('The RSS of predicting Prices based on Square Feet is : ' + str(rss_prices_on_sqft))


# In[17]:


def inverse_regression_predictions(output, intercept, slope):
    # solve output = intercept + slope*input_feature for input_feature. Use this equation to compute the inverse predictions:
    estimated_feature = (output - intercept)/slope
    return estimated_feature


# In[18]:


my_house_price = 800000
estimated_squarefeet = inverse_regression_predictions(my_house_price, sqft_intercept, sqft_slope)
print ("The estimated squarefeet for a house worth $%.2f is %d" % (my_house_price, estimated_squarefeet))


# In[19]:


# Estimate the slope and intercept for predicting 'price' based on 'bedrooms'
sqft_intercept, sqft_slope = simple_linear_regression(train_data['bedrooms'], train_data['price'])

print ("Intercept: " + str(sqft_intercept))
print ("Slope: " + str(sqft_slope))


# In[20]:


# Compute RSS when using bedrooms on TEST data:
sqft_intercept, sqft_slope = simple_linear_regression(train_data['bedrooms'], train_data['price'])
rss_prices_on_bedrooms = get_residual_sum_of_squares(test_data['bedrooms'], test_data['price'], sqft_intercept, sqft_slope)
print ('The RSS of predicting Prices based on Bedrooms is : ' + str(rss_prices_on_bedrooms))


# In[21]:


# Compute RSS when using squarfeet on TEST data:
sqft_intercept, sqft_slope = simple_linear_regression(train_data['sqft_living'], train_data['price'])
rss_prices_on_sqft = get_residual_sum_of_squares(test_data['sqft_living'], test_data['price'], sqft_intercept, sqft_slope)
print ('The RSS of predicting Prices based on Square Feet is : ' + str(rss_prices_on_sqft))


# In[ ]:




