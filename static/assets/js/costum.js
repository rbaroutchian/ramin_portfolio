$(document).ready(function () {
    $("#contact-form").submit(function (event) {
        event.preventDefault();

        Swal.fire({
            title: "در حال ارسال...",
            text: "لطفاً منتظر بمانید.",
            icon: "info",
            showConfirmButton: false,
            timer: 1500
        });

        $.ajax({
            type: "POST",
            url: $(this).attr("action"),
            data: $(this).serialize(),
            success: function (response) {
                Swal.fire({
                    title: "موفق!",
                    text: response.message,
                    icon: "success",
                    confirmButtonText: "باشه"
                });
                $("#contact-form")[0].reset();
            },
            error: function () {
                Swal.fire({
                    title: "خطا!",
                    text: "مشکلی رخ داده است.",
                    icon: "error",
                    confirmButtonText: "تلاش مجدد"
                });
            }
        });
    });
});




