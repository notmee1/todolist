# todolist
Dự án đơn giản về app Todo-list được viết bằng HTML, CSS và Javascript
# Test
``pip install selenium`` và sử dụng script test
# Tài liệu về Ứng dụng To Do List
## Mô tả
Ứng dụng To Do List là một ứng dụng web đơn giản được xây dựng bằng HTML, CSS và JavaScript. Nó cho phép người dùng thêm việc cần làm vào một danh sách. Danh sách sau đó được lưu vào bộ nhớ lưu trữ cục bộ (localStorage) của trình duyệt, do đó người dùng có thể tải lại trang mà không mất danh sách hiện tại. Bên cạnh mỗi mục trong danh sách, một nút "Delete" được cung cấp để người dùng có thể xóa mục đó khỏi danh sách

## Ứng dụng
Ứng dụng này có thể được sử dụng để theo dõi các việc cần làm trong ngày. Do dữ liệu được lưu vào bộ nhớ lưu trữ cục bộ, người dùng có thể thoát ra khỏi trình duyệt hoặc tải lại trang mà không lo mất dữ liệu

## Kỹ thuật
### Mô hình DOM
Ứng dụng sử dụng Mô hình Đối tượng Tài liệu (DOM) để thêm hoặc xóa các phần tử HTML từ trang web và sửa đổi nội dung của chúng
### localStorage
LocalStorage là một dạng bộ nhớ web cho phép các trang web lưu trữ dữ liệu theo dạng cặp key-value trong trình duyệt của người dùng. Dữ liệu được lưu trữ không có thời hạn hết hạn, để lại điều này cho người dùng hoặc trang web. Điều này cho phép dữ liệu tồn tại ngay cả sau khi trang đã được tải lại
### Sự kiện JavaScript
Ứng dụng sử dụng sự kiện JavaScript để xử lý việc nhấp chuột người dùng, cho phép các hành động nhất định được kích hoạt khi điều này xảy ra. Sự kiện 'onclick' được sử dụng để xác định hành động thêm một việc mới vào danh sách hoặc xóa một việc hiện tại khỏi danh sách
### JSON
Ứng dụng sử dụng JSON (JavaScript Object Notation), một định dạng dữ liệu dễ đọc và viết và được sử dụng để lưu trữ và trao đổi dữ liệu. Trong trường hợp này, JSON được sử dụng để lưu dữ liệu dưới dạng string khi đặt vào localStorage và sau đó phân tách dữ liệu string đó trở lại thành object JavaScript khi lấy ra từ localStorage
