
    const products = [
      {
        id: 1,
        name: "Продукт 1",
        image: "https://via.placeholder.com/300",
        unit: "шт",
        price: "100₽",
      },
      {
        id: 2,
        name: "Продукт 2",
        image: "https://via.placeholder.com/300",
        unit: "шт",
        price: "200₽",
      },
      {
        id: 3,
        name: "Продукт 3",
        image: "https://via.placeholder.com/300",
        unit: "шт",
        price: "300₽",
      },
    ];

    const productContainer = document.getElementById('product-container');

    // Создаем элементы продуктов
    products.forEach(product => {
      const productElement = document.createElement('div');
      productElement.classList.add('article-summary', 'is_prod');
      productElement.setAttribute('data-product-id', product.id);

      productElement.innerHTML = `
        <img src="${product.image}" alt="${product.name}">
        <div class="article-summary-content">
          <h2>${product.name}</h2>
          <p>Единица измерения: ${product.unit}</p>
          <p>Цена: ${product.price}</p>
        </div>
      `;

      productContainer.appendChild(productElement);
    });

    // Добавляем эффект параллакса для каждого элемента
    document.querySelectorAll('.article-summary').forEach((summary) => {
      const content = summary.querySelector('.article-summary-content');
      const image = summary.querySelector('img');

      summary.addEventListener('mousemove', (e) => {
        const rect = summary.getBoundingClientRect();
        const x = ((e.clientX - rect.left) / rect.width - 0.5) * 20; // Движение по X
        const y = ((e.clientY - rect.top) / rect.height - 0.5) * 20; // Движение по Y

        // Смещение содержимого
        content.style.transform = `translate(${x}px, ${y}px)`;
        image.style.transform = `translate(${x / 2}px, ${y / 2}px)`; // Легкое смещение изображения
      });

      // Возврат содержимого на место при выходе мыши
      summary.addEventListener('mouseleave', () => {
        content.style.transform = `translate(0, 0)`;
        image.style.transform = `translate(0, 0)`;
      });
    });