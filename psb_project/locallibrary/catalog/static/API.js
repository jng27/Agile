function postJSON(csrftoken, url, postData, onsuccess, onerror) {
    $.ajax({
        type: "POST",
        headers: { "X-CSRFToken": csrftoken },
        url: url,
        data: JSON.stringify(postData),
        success: function (data) {
            onsuccess(data)
        },
        error: function (err) {
            onerror(err)
        },
        contentType: 'application/json;',
        dataType: 'json',
    });
}