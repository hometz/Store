document.addEventListener("DOMContentLoaded", () => {
    const navbar = document.querySelector(".navbar");

    navbar.addEventListener("click", e => {
        if (e.target.classList.contains("tab")) {
            e.preventDefault();
            window.location.href = `/${e.target.id}` 
        }
    });

    document.querySelectorAll(".article-summary").forEach(item => {
        item.addEventListener("click", e => {
            if (!e.target.classList.contains("edit") && !e.target.classList.contains("reviews_cls")) {
                const articleSummary = e.target.closest(".article-summary");
                const productId = articleSummary.getAttribute("data-product-id");
                console.log("Product ID:", productId); // Добавлено для отладки
                window.location.href = `/products/${productId}/detail/`;
            }
        });
    });
});