var clg3 = (function () {
    var init, msg;

    msg = "U2FsdGVkX18CV90Qh4/Cht/K4SXqjhehwz7Z+pKoHEaYM+hj9Kr7RQtmWhs95E0qEdd31Ifve+3RhK5Ve3eiRGAVQIrzv9HYrHmHNIZHH0OkH4QDeTlDez6lRDit2wtZszgxttF1IUqUfDAf38l++B7LeLszjh7vV67PXlXNjZB/ktNm8rfvrN+BRKzU3H0sSd7XGnF8GOyXTwwuZuC5/6WzdIbTsVVCPn3CCMpNzEEwgHCK0Ee1/BFP6xbOSVWG9V3j8kqo9Dm1srMpjkvP1JcVeu7yLRU1NCfyN2gOgd7uLVM33wPHdy/rV4Gnq/btM2cv6Q/YiqCM3/PWnaZ67b1Vsj0Yf73clSqOwd0kirPOK2fmhvKXrqBCebYjmuuFF3MMuY/2dsv5eLinCq0C100/j0WYvz40S9TYY3dNg4Fl4WdRmyFj8cBqoSvlEhYYTd12suLNeBH3rv5SwboStFktqQmBAI841nTm2pR6z0heGpM9dEDLU5jUGhXY00DLjGX86HSBz4qfldozUxgvhHYkwYl9mGvaID4wBnmojY3Q0U7J/MURkktCrAO196mMIqrzLcy7gte71oxdFWBZWi18AcT4XOA7tt7QithYZasX51CPmey8YMxtSunsfNzPygTkARHCWAk8CIqMF+/miSeyNz4719ub/isb23uubnbrLZo4SFowCNGV4R2lJiy5iVtqTrE1U5NP+6L3cDgoCTFhnAIv2V3mcNayIhntheQZI76UlS22GFYK79Y+rmpp3sLxUSQwz2ZGfeqTpR/l0V2AVbfsmXyUtdUdbQjQfzCha1VOmTgelDRnwACQD60s/+zrUDwxTL5Thjh0hrBMPy0jLd/JzZENJZ4R4doVWG4YotgHGHWk+k3csJ5AUmroAl3gEeEi1Xbxm/a5F+m3i8OtFqmSBH98ZXvj07qwWUlp9tuaC1YcQyCDRcTbtjENE9QHW3vRj7nH02K9y+YO7idHldL/ZcvlvHBMhw+FnCMkttgD3q4O3X3i9GknpVzl"

    init = function () {
        $("#btn_activate").click(function () {
            var arg1 = $("input[name=code1]").val(),
                arg2 = $("input[name=code2]").val(),
                password = arg1+arg2,
                decrypted = "Invalid Code";

            if (!arg1 || !arg2)
                return

            // var encrypted = CryptoJS.AES.encrypt("", password);
            // console.log(encrypted.toString())
            try {
                decrypted = CryptoJS.AES.decrypt(msg, password).toString(CryptoJS.enc.Utf8);
            }
            catch(error) {
                
            }
            $("#div_rst").html(decrypted)
        })

        $("#btn_test").click(function () {
            var btn = $(this),
                url = ""
        })

    }

    return {
        init: init
    }
})()
