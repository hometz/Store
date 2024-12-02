document.addEventListener("DOMContentLoaded", () => {
    const tabs = document.querySelectorAll(".tab");
    const currentPath = window.location.pathname;
    const menuToggle = document.querySelector('.menu-toggle');
    const mobileMenu = document.getElementById('mobileMenu');
    const productContainer = document.getElementById('productContainer');
    const pagination = document.getElementById('pagination');
    let currentPage = 1;

    menuToggle.addEventListener('click', () => {
        mobileMenu.style.display = mobileMenu.style.display === 'flex' ? 'none' : 'flex';
    });

    tabs.forEach(tab => {
        if (`/${tab.id}/` === currentPath) {
            SetActive(tab);
        }
    });

    tabs.forEach(e => {
        e.addEventListener("click", event => {
            event.preventDefault();
            window.location.href = `/${event.target.id}`;
        });
    });

    async function loadProducts(page = 1) {
        try {
            const response = await fetch(`/api/products/?page=${page}`);
            const data = await response.json();
            renderProducts(data.products);
            renderPagination(data);
        } catch (error) {
            console.error("Ошибка загрузки данных:", error);
        }
    }

    function renderProducts(products) {
        productContainer.innerHTML = '';

        products.forEach(product => {
            const productElement = document.createElement('div');
            productElement.classList.add('article-summary', 'is_prod');
            productElement.setAttribute('data-product-id', product.id);
            productElement.innerHTML = `
                <img src="${product.image}" alt="${product.name}" width="250">
                <h2>big ${product.name}</h2>
                <p>Единица измерения: ${product.unit}</p>
                <p>Цена: ${product.price}</p>
            `;
            productContainer.appendChild(productElement);
        });

        handleProductClick();
    }

    function renderPagination(data) {
        pagination.innerHTML = '';

        const prevButton = document.createElement('button');
        prevButton.textContent = '<';
        prevButton.disabled = !data.has_previous;
        prevButton.addEventListener('click', () => {
            if (data.has_previous) {
                currentPage = data.previous_page_number;
                loadProducts(currentPage);
            }
        });
        pagination.appendChild(prevButton);

        const currentPageIndicator = document.createElement('span');
        currentPageIndicator.textContent = `${data.current_page}/${data.total_pages}`;
        pagination.appendChild(currentPageIndicator);

        const nextButton = document.createElement('button');
        nextButton.textContent = '>';
        nextButton.disabled = !data.has_next;
        nextButton.addEventListener('click', () => {
            if (data.has_next) {
                currentPage = data.next_page_number;
                loadProducts(currentPage);
            }
        });
        pagination.appendChild(nextButton);
    }

    function handleProductClick() {
        const summary = document.querySelectorAll('.article-summary');
        
        summary.forEach(item => {
            item.addEventListener("click", e => {
                if (!e.target.classList.contains("edit") && !e.target.classList.contains("reviews_cls")) {
                    const articleSummary = e.target.closest(".article-summary");
                    const productId = articleSummary.getAttribute("data-product-id");
                    window.location.href = `/products/${productId}/detail/`;
                }
            });
        });
    }

    loadProducts(currentPage);

    function SetActive(currTab) {
        currTab.classList.add("active");
    }
});
