// 添加销售人员表单提交事件处理程序
document
  .querySelector('form[action="/add_salesperson"]')
  .addEventListener('submit', function (event) {
    event.preventDefault(); // 阻止表单默认提交行为
    var form = event.target;
    var formData = new FormData(form);

    // 使用Ajax提交表单数据
    fetch(form.action, {
      method: 'POST',
      body: formData,
    })
      .then(function (response) {
        if (response.status === 200) {
          // 表单提交成功，显示成功消息并重置表单
          alert('Salesperson added successfully!');
          form.reset();
        } else {
          // 表单提交失败，显示错误消息
          alert('Failed to add salesperson. Please try again.');
        }
      })
      .catch(function (error) {
        // 捕获网络请求错误
        alert('An error occurred while adding salesperson. Please try again.');
        console.error(error);
      });
  });

// 添加消息椅子表单提交事件处理程序
document
  .querySelector('form[action="/add_chair"]')
  .addEventListener('submit', function (event) {
    event.preventDefault(); // 阻止表单默认提交行为
    var form = event.target;
    var formData = new FormData(form);

    // 使用Ajax提交表单数据
    fetch(form.action, {
      method: 'POST',
      body: formData,
    })
      .then(function (response) {
        if (response.status === 200) {
          // 表单提交成功，显示成功消息并重置表单
          alert('Massage chair added successfully!');
          form.reset();
        } else {
          // 表单提交失败，显示错误消息
          alert('Failed to add massage chair. Please try again.');
        }
      })
      .catch(function (error) {
        // 捕获网络请求错误
        alert(
          'An error occurred while adding massage chair. Please try again.'
        );
        console.error(error);
      });
  });

// 添加顾客表单提交事件处理程序
document
  .querySelector('form[action="/add_customer"]')
  .addEventListener('submit', function (event) {
    event.preventDefault(); // 阻止表单默认提交行为
    var form = event.target;
    var formData = new FormData(form);

    // 使用Ajax提交表单数据
    fetch(form.action, {
      method: 'POST',
      body: formData,
    })
      .then(function (response) {
        if (response.status === 200) {
          // 表单提交成功，显示成功消息并重置表单
          alert('Customer added successfully!');
          form.reset();
        } else {
          // 表单提交失败，显示错误消息
          alert('Failed to add customer. Please try again.');
        }
      })
      .catch(function (error) {
        // 捕获网络请求错误
        alert('An error occurred while adding customer. Please try again.');
        console.error(error);
      });
  });
