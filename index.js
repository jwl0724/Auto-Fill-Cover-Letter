let modal = document.getElementById("example");
let showModal = document.getElementById("openExample");

showModal.addEventListener("click", () => {
    modal.showModal();
    let closeButton = document.getElementById("closeModal");
    closeButton.addEventListener("click", () => {
        modal.close();
    });
});