$('document').ready(function () {
    let toggle = $('.combo-field-toggle');
    let passwordField = $('.combo-field.password-field');

    toggle.on('click', function () {
        if (passwordField.attr('type') === 'password') {
            passwordField.attr('type', 'text');
            toggle.children().addClass('fa-eye').removeClass('fa-eye-slash');
        } else {
            passwordField.attr('type', 'password');
            toggle.children().addClass('fa-eye-slash').removeClass('fa-eye');
        }
    })
});
let numberOfEvent = $('.grid a').length;
console.log(numberOfEvent)
let limitEvent = 9;
$(".grid a:gt(" + (limitEvent - 1) + ")").hide();
let totalPages = Math.round(numberOfEvent / limitEvent);
if ((numberOfEvent / limitEvent) > Math.round(numberOfEvent / limitEvent)) {
    totalPages = Math.round(numberOfEvent / limitEvent + 1);
}
console.log(totalPages)
let currentPage = $(".pagination p").text();
console.log(currentPage)

$(".pagination li.next").on("click", function () {
    if (currentPage == totalPages || totalPages == 0) {
        return false;
    } else {
        currentPage++;
        $('.pagination li').removeClass("active")
        $('.grid a').hide();
        change_page();
    }
})

$(".pagination li.previous").on("click", function () {
    if (currentPage == 1) {
        return false;
    } else {
        currentPage--;
        $('.pagination li').removeClass("active")
        $('.grid a').hide();
        change_page();
    }
})

function change_page() {
    let grandTotal = limitEvent * currentPage
    for (let i = grandTotal - limitEvent; i < grandTotal; i++) {
        $(".grid a:eq(" + (i) + ")").show();
    }
    $(".pagination li.page-current").addClass("active");
    $(".pagination p").text(currentPage);
}
