# Logistic Regression 
1. Phải one hot encode ( vì nó chỉ chấp nhân 0,1)

Minmaxscaler ( set min = 0.1 sẽ tốt hơn. Vì scale từ 0 thì nhân vào nó bằng 0 mất)


# Essamble learning 

Kết hợp nhiều model lại với nhau 
Có 3 cách
1. Training nhiều model rồi lấy predict value trung bình 
2. Training nối tiếp 
3. 

## Bagging 

Train 100 tập data set ra 100 model 
committee square error 

## random forest:
Là 1 thuật toán bagging. Đi thực hiện bootstrap. Decision tree rồi chia trung bình 
Giả sử random forest với n tree = n_estimator = 100 

Khác với bagging mà ko chia trung bình mà xài voting model ( chọn số lượng đông )

## AdaBoost ( adatpive boosting )



## tuning regularization
cost = (y-h)^2

những yếu tố ko nằm trong mô hình 


# cách chọn feature 
Cách chọn feature dựa trên phân phối

Thời gian bay là giá trị liên tục Biến dự đoán là category

PHân ra 2: LateArr = 0 or 1 Phân phối có giống nhau ko?

Nếu biến là category. vd hãng bay khảo sát sl delay trong A, ko delay trong A Xét về % delay của 2 hãng A,B Nếu giống nhau: ko phải là feature Nếu 2 hãng delay khác nhau thì đó là feature

# Reference

## Imbalance: 
dữ liệu ko cân bằng, sl số 1 và 0 là rất khác nhau ( giả sử 0 rất nhiều 90%)
Model mình ko làm gì cả và phán tất cả là 0 

P = 0.9
R = 0 (recall)
=> F(0) = 0 ko học dc gì
### Cách 1: Tìm thuật toán robust with imbalance: decision tree , naive bayes, knn 

### Cách 2: Điều chỉnh threshold
Logistic regression:
>0.5 coi như 1, < 0.5 coi như 0 
predict_proba() -> xác suất là số 1, 0

Điều chỉnh threshold của model 0.3

### Cách 3: Điều chỉnh cost function 
cost = y*log(1-y) + (1-y)log(1-y)
ylog(1-y) : là số 1
(1-y)log(1-y) : là số 0
Để thay đổi cost mình nhân thêm tham số alpha
cost = alpha*y*log(1-y) + (1-alpha)(1-y)log(1-y)
Tức là nếu dự đoán sai số 1, thì cost lớn hơn nhiều so với dự đoán sai số 0


### Cách 4: resampling
Chọn radom 10 làn trong data số 0
- up sample 
- down sample 

Logistic regression


# SVM 

## Maximum margim 