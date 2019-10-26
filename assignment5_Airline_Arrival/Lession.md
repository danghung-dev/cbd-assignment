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