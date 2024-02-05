import matplotlib.pyplot as plt

# Generate predictions with confidence intervals
pred = model_fit.get_prediction(start=len(train_data), end=len(train_data)+len(test_data)-1, dynamic=False)
pred_conf = pred.conf_int()
# Plot the predictions with confidence intervals
plt.figure(figsize=(14, 7))
plt.plot(history.index[:len(train_data)], train_data, label='Train')
plt.plot(history.index[len(train_data):], test_data, label='Test')
plt.plot(history.index[len(train_data):], predictions, label='Predicted')
plt.fill_between(history.index[len(train_data):], pred_conf[:,0], pred_conf[:,1], color='g', alpha=0.3)
plt.title('Bitcoin Closing Price with ARIMA Predictions and Confidence Intervals')
plt.xlabel('Date')
plt.ylabel('Closing Price (USD)')
plt.legend()
plt.grid(True)
plt.savefig('/app/static/uploads/btc_arima_confidence_intervals.png')
plt.close()