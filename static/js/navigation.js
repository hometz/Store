
function SetActive(currTab) {
    currTab.classList.add("active");
}

document.addEventListener("DOMContentLoaded", () => {
    const tabs = document.querySelectorAll(".tab");
    const currentPath = window.location.pathname;

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