grecaptcha.ready(function () {
  grecaptcha.execute("6LciphsgAAAAAHqc_MiIMvPhMfKZSVjUMP12znWX", {action: "validate_captcha"}).then(function (token) {
    console.info("got token: " + token);
    document.getElementById("g-recaptcha-response").value = token;
  });
});
