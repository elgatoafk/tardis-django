function displayRadioValue() {
            var ele = document.getElementsByName("time-zone");

            for (i = 0; i < ele.length; i++) {
                if (ele[i].checked)
                    window.result_zone
                        = "Results shown for " + ele[i].value +" time zone.";
            }
        }
document.getElementsByName("time-zone").addEventListener("click", displayRadioValue);