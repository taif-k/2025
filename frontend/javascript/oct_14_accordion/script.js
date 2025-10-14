document.addEventListener("DOMContentLoaded", function () {
    const headers = Array.from(document.querySelectorAll(".accordion-header"));
    // console.log(headers);

    headers.forEach(header => {
        header.addEventListener("click", function () {
            const content = this.nextElementSibling;
            const openTab = this.getAttribute("aria-expanded") === "true";
            // console.log(content)


            const Contents = Array.from(document.querySelectorAll(".accordion-content"));

            Contents.forEach(content => content.style.display = "none");
            headers.forEach(headr => headr.setAttribute("aria-expanded", "false"));
            document.querySelectorAll(".accordion-header .icon").forEach(icon => icon.textContent = "+");

            if (openTab == false) {
                this.setAttribute("aria-expanded", "true");
                content.style.display = "block";
                this.querySelector(".icon").textContent = "-";
            }
        });
    });
});
