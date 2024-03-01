document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.confirm-database-import-form');
    const csrf_token = form.dataset.csrfToken;

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        form.classList.add('loading-mask', 'loading');

        const formData = new FormData(form);

        const requestData = {
            method: form.method,
            body: formData,
            headers: {
                'X-CSRFToken': csrf_token,
            }
        }

        fetch(form.action, requestData)
            .then(response => response.json())
        .then(data => {
            form.classList.remove('loading-mask', 'loading');
            if (data.error) {
                alert(data.error);
                return;
            }
            const nextUrl = data.next_url;
            if (nextUrl) {
                window.location.href = nextUrl;
            } else {
                alert('Something went wrong...');
            }
        }).catch(error => {
            form.classList.remove('loading-mask', 'loading');
            alert('Something went wrong...');
        });
    });
});
