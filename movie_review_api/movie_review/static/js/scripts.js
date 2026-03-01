

document.addEventListener("DOMContentLoaded", () => {


    const likeButtons = document.querySelectorAll(".like-btn");
    likeButtons.forEach(button => {
        button.addEventListener("click", async (e) => {
            e.preventDefault();
            const reviewId = button.dataset.reviewId;
            
            try {
                const response = await fetch(`/reviews/${reviewId}/like/`, {
                    method: "POST",
                    headers: {
                        "X-CSRFToken": getCookie("csrftoken")
                    }
                });
                if(response.ok){
                    const data = await response.json();
                    button.innerText = `❤️ ${data.likes_count}`;
                }
            } catch(err) {
                console.error("Error liking review:", err);
            }
        });
    });

    // CSRF token helper
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== "") {
            const cookies = document.cookie.split(";");
            for (let cookie of cookies) {
                cookie = cookie.trim();
                if (cookie.startsWith(name + "=")) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

});