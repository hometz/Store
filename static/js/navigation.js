document.addEventListener("DOMContentLoaded", () => {
    const navbar = document.querySelector(".navbar");

    navbar.addEventListener("click", e => {
        if (e.target.classList.contains("tab")) {
            e.preventDefault();
            window.location.href = `/${e.target.id}` 
        }
    });

    console.log(window.location.href);

    document.querySelectorAll(".article-summary").forEach(item => {
        item.addEventListener("click", e => {
            if (!e.target.classList.contains("edit") 
                && !e.target.classList.contains("reviews_cls")
                && item.classList.contains("is_prod")) {
                const articleSummary = e.target.closest(".article-summary");
                const productId = articleSummary.getAttribute("data-product-id");
                window.location.href = `/products/${productId}/detail/`;
            }
        });
    });

    
});