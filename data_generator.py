import pandas as pd
import random
import datetime

data = []
start_date = datetime.date(2023, 5, 1)
end_date = datetime.date(2023, 5, 31)

for i in range((end_date - start_date).days + 1):
    date = start_date + datetime.timedelta(days=i)
    formatted_date = date.strftime("%m/%d/%Y")  
    price = random.randint(80, 200)
    occupancy_rate = round(random.uniform(0.7, 1.0), 2)
    competitor_price = random.randint(80, 200)
    temperature = random.randint(20, 35)
    precipitation = random.randint(0, 10) / 10.0
    holiday = random.choice([0, 1])
    event = random.choice([0, 1])
    
    
    day_of_week = date.weekday() 
    month = date.month
    is_weekend = 1 if day_of_week >= 5 else 0
    price_last_week = random.randint(80, 200)  
    rolling_avg_week = random.randint(80, 200)  
    
    
    data.append([formatted_date, price, occupancy_rate, competitor_price, temperature, precipitation, 
                 holiday, event, day_of_week, month, is_weekend, price_last_week, rolling_avg_week])


df = pd.DataFrame(data, columns=['date', 'price', 'occupancy_rate', 'competitor_price', 'temperature', 
                                  'precipitation', 'holiday', 'event', 'day_of_week', 'month', 'is_weekend', 
                                  'price_last_week', 'rolling_avg_week'])


df.to_csv('hotel_prices.csv', index=False)
