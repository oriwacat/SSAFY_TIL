# import json  
# from pathlib import Path  


# file_path = Path('./data/books_20.json')  


# if file_path.exists():  
    
#     with file_path.open('r', encoding='utf-8') as file:
#         data = json.load(file)  

   
#     book_prices = []  
#     for item in data['item']:  
#         book_prices.append(item['priceSales'])  

    
#     average_price = (sum(book_prices) / len(book_prices))  

    
#     print(f"도서 평균 가격: {average_price:.2f}원")

# else:
    
#     print(f"파일이 존재하지 않습니다: {file_path}")  

number = [1, 2, 3, 4, 5]

squared2 = list(map(lambda x : x**2, number))
print(squared2)