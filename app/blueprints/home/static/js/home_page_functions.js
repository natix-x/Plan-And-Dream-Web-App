/**
 * Deletes user from db by fetching from delete_user url and redirects him to home page for not logged in users.
 * @param {string} userId Id of user to be deleted
 */
function deleteUserAndRedirect(userId) {
    fetch(`/delete_user/${userId}`, {
            method: "POST"
        })
        .then(response => {
            if (!response.ok) {
                throw new Error("Failed to delete selected user.");
            }
            else {console.log("success")}
            window.location.href = '/home'
        });
}
