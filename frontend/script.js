// let previousAlert = null;


// // =====================================
// // GET FARM STATUS
// // =====================================

// async function fetchFarmStatus() {

//     try {

//         const response = await fetch(
//             "/farm-status"
//         );


//         if (!response.ok) {

//             throw new Error(
//                 `HTTP ${response.status}`
//             );

//         }


//         const data = await response.json();


//         updateDashboard(data);


//     } catch (error) {

//         console.error(
//             "Farm status error:",
//             error
//         );

//         setOfflineStatus();

//     }

// }


// // =====================================
// // UPDATE DASHBOARD
// // =====================================

// function updateDashboard(data) {


//     // -------------------------------
//     // CONNECTION
//     // -------------------------------

//     const status =
//         document.getElementById(
//             "connectionStatus"
//         );


//     if (data.connected) {

//         status.innerHTML =
//             '<span class="dot"></span> SENSOR CONNECTED';

//     } else {

//         status.innerHTML =
//             '<span class="dot"></span> WAITING FOR SENSOR';

//     }


//     // -------------------------------
//     // SENSOR DATA
//     // -------------------------------

//     document.getElementById(
//         "temperature"
//     ).innerText =
//         data.tempreature !== null
//             ? `${data.tempreature} °C`
//             : "-- °C";


//     document.getElementById(
//         "humidity"
//     ).innerText =
//         data.humidity !== null
//             ? `${data.humidity} %`
//             : "-- %";


//     document.getElementById(
//         "soilMoisture"
//     ).innerText =
//         data.soil_moisture !== null
//             ? `${data.soil_moisture} %`
//             : "-- %";


//     // -------------------------------
//     // FARM INFORMATION
//     // -------------------------------

//     document.getElementById(
//         "crop"
//     ).innerText =
//         data.crop || "---";


//     document.getElementById(
//         "cropStage"
//     ).innerText =
//         data.crop_stage || "---";


//     document.getElementById(
//         "soilType"
//     ).innerText =
//         data.soil_type || "---";


//     document.getElementById(
//         "area"
//     ).innerText =
//         data.area || "---";


//     // -------------------------------
//     // AI
//     // -------------------------------

//     document.getElementById(
//         "observation"
//     ).innerText =
//         data.observation ||
//         "Waiting for AI...";


//     document.getElementById(
//         "decision"
//     ).innerText =
//         data.decision || "---";


//     document.getElementById(
//         "actionType"
//     ).innerText =
//         data.action_type || "---";


//     // -------------------------------
//     // HARDWARE
//     // -------------------------------

//     document.getElementById(
//         "hardwareCommand"
//     ).innerText =
//         data.hardware_command ??
//         "---";


//     document.getElementById(
//         "executedAction"
//     ).innerText =
//         data.executed_action ||
//         "---";


//     // -------------------------------
//     // SAFETY
//     // -------------------------------

//     document.getElementById(
//         "safetyStatus"
//     ).innerText =
//         data.safety_status ||
//         "WAITING";


//     document.getElementById(
//         "safetyReason"
//     ).innerText =
//         data.safety_reason ||
//         "---";


//     // -------------------------------
//     // VERIFICATION
//     // -------------------------------

//     document.getElementById(
//         "verificationStatus"
//     ).innerText =
//         data.verification_status ||
//         "---";


//     document.getElementById(
//         "verificationMessage"
//     ).innerText =
//         data.verification_message ||
//         "---";


//     // -------------------------------
//     // ALERT
//     // -------------------------------

//     const alertElement =
//         document.getElementById(
//             "alert"
//         );


//     if (data.alert) {

//         alertElement.innerText =
//             "🚨 " + data.alert;

//     } else {

//         alertElement.innerText =
//             "No active alerts.";

//     }


//     // -------------------------------
//     // FINAL RESPONSE
//     // -------------------------------

//     document.getElementById(
//         "response"
//     ).innerText =
//         data.response ||
//         "---";


//     // -------------------------------
//     // RAW API DATA
//     // -------------------------------

//     document.getElementById(
//         "rawJson"
//     ).innerText =
//         JSON.stringify(
//             data,
//             null,
//             2
//         );


//     // -------------------------------
//     // NOTIFICATION
//     // -------------------------------

//     handleNotification(data);

// }


// // =====================================
// // NOTIFICATIONS
// // =====================================

// function handleNotification(data) {

//     if (!data.alert) {

//         previousAlert = null;

//         return;

//     }


//     if (
//         data.alert !== previousAlert
//     ) {

//         sendNotification(
//             "ROBOAI Alert",
//             data.alert
//         );

//         previousAlert =
//             data.alert;

//     }

// }


// // =====================================
// // BROWSER NOTIFICATION
// // =====================================

// function sendNotification(
//     title,
//     message
// ) {

//     if (
//         Notification.permission ===
//         "granted"
//     ) {

//         new Notification(
//             title,
//             {
//                 body: message,
//                 icon: "/static/icon.png"
//             }
//         );

//     }

// }


// // =====================================
// // ENABLE NOTIFICATIONS
// // =====================================

// document
//     .getElementById(
//         "notificationBtn"
//     )
//     .addEventListener(
//         "click",
//         async () => {

//             if (
//                 !("Notification" in window)
//             ) {

//                 alert(
//                     "Browser notifications are not supported."
//                 );

//                 return;

//             }


//             const permission =
//                 await Notification.requestPermission();


//             if (
//                 permission ===
//                 "granted"
//             ) {

//                 alert(
//                     "Notifications enabled."
//                 );

//             }

//         }
//     );


// // =====================================
// // REFRESH
// // =====================================

// document
//     .getElementById(
//         "refreshBtn"
//     )
//     .addEventListener(
//         "click",
//         fetchFarmStatus
//     );


// // =====================================
// // CLEAR
// // =====================================

// document
//     .getElementById(
//         "clearBtn"
//     )
//     .addEventListener(
//         "click",
//         () => {

//             document.getElementById(
//                 "observation"
//             ).innerText =
//                 "Waiting for sensor data...";


//             document.getElementById(
//                 "decision"
//             ).innerText =
//                 "---";


//             document.getElementById(
//                 "actionType"
//             ).innerText =
//                 "---";


//             document.getElementById(
//                 "hardwareCommand"
//             ).innerText =
//                 "---";


//             document.getElementById(
//                 "executedAction"
//             ).innerText =
//                 "---";


//             document.getElementById(
//                 "safetyStatus"
//             ).innerText =
//                 "WAITING";


//             document.getElementById(
//                 "safetyReason"
//             ).innerText =
//                 "---";


//             document.getElementById(
//                 "verificationStatus"
//             ).innerText =
//                 "---";


//             document.getElementById(
//                 "verificationMessage"
//             ).innerText =
//                 "---";


//             document.getElementById(
//                 "alert"
//             ).innerText =
//                 "No active alerts.";


//             document.getElementById(
//                 "response"
//             ).innerText =
//                 "Waiting for graph execution...";


//             document.getElementById(
//                 "rawJson"
//             ).innerText =
//                 "{}";

//         }
//     );


// // =====================================
// // AUTOMATIC POLLING
// // =====================================

// // Get latest farm data immediately

// fetchFarmStatus();


// // Then check every 3 seconds

// setInterval(
//     fetchFarmStatus,
//     3000
// );

// const saveFarmBtn = document.getElementById("saveFarmBtn");

// if (saveFarmBtn) {

//     saveFarmBtn.addEventListener("click", async () => {

//         const crop = document.getElementById("crop").value;
//         const cropStage = document.getElementById("cropStage").value;
//         const soilType = document.getElementById("soilType").value;
//         const area = document.getElementById("area").value.trim();


//         if (!area) {

//             document.getElementById("farmSetupMessage").textContent =
//                 "Please enter the farm area.";

//             return;
//         }


//         const farmData = {
//             crop: crop,
//             crop_stage: cropStage,
//             soil_type: soilType,
//             area: area
//         };


//         try {

//             const response = await fetch("/farm-setup", {

//                 method: "POST",

//                 headers: {
//                     "Content-Type": "application/json"
//                 },

//                 body: JSON.stringify(farmData)
//             });


//             const data = await response.json();


//             if (response.ok) {

//                 document.getElementById("farmSetupMessage").textContent =
//                     "Farm profile saved successfully.";

//                 console.log("Farm profile:", data.farm_profile);

//             } else {

//                 document.getElementById("farmSetupMessage").textContent =
//                     "Failed to save farm profile.";
//             }


//         } catch (error) {

//             console.error(error);

//             document.getElementById("farmSetupMessage").textContent =
//                 "Connection error.";
//         }

//     });
// }

let previousAlert = null;


// =====================================
// GET FARM STATUS
// =====================================

async function fetchFarmStatus() {

    try {

        const response = await fetch(
            "/farm-status"
        );

        if (!response.ok) {

            throw new Error(
                `HTTP ${response.status}`
            );

        }

        const data = await response.json();

        updateDashboard(data);

    } catch (error) {

        console.error(
            "Farm status error:",
            error
        );

        setOfflineStatus();

    }

}


// =====================================
// OFFLINE STATUS
// =====================================

function setOfflineStatus() {

    const status =
        document.getElementById(
            "connectionStatus"
        );

    if (status) {

        status.innerHTML =
            '<span class="dot"></span> CONNECTION ERROR';

    }

}


// =====================================
// UPDATE DASHBOARD
// =====================================

function updateDashboard(data) {


    // -------------------------------
    // CONNECTION
    // -------------------------------

    const status =
        document.getElementById(
            "connectionStatus"
        );


    if (status) {

        if (data.connected) {

            status.innerHTML =
                '<span class="dot"></span> SENSOR CONNECTED';

        } else {

            status.innerHTML =
                '<span class="dot"></span> WAITING FOR SENSOR';

        }

    }


    // -------------------------------
    // SENSOR DATA
    // -------------------------------

    document.getElementById(
        "temperature"
    ).innerText =
        data.tempreature !== null &&
        data.tempreature !== undefined
            ? `${data.tempreature} °C`
            : "-- °C";


    document.getElementById(
        "humidity"
    ).innerText =
        data.humidity !== null &&
        data.humidity !== undefined
            ? `${data.humidity} %`
            : "-- %";


    document.getElementById(
        "soilMoisture"
    ).innerText =
        data.soil_moisture !== null &&
        data.soil_moisture !== undefined
            ? `${data.soil_moisture} %`
            : "-- %";


    // -------------------------------
    // FARM INFORMATION
    // -------------------------------

    document.getElementById(
        "crop"
    ).innerText =
        data.crop || "---";


    document.getElementById(
        "cropStage"
    ).innerText =
        data.crop_stage || "---";


    document.getElementById(
        "soilType"
    ).innerText =
        data.soil_type || "---";


    document.getElementById(
        "area"
    ).innerText =
        data.area || "---";


    // -------------------------------
    // AI
    // -------------------------------

    document.getElementById(
        "observation"
    ).innerText =
        data.observation ||
        "Waiting for AI...";


    document.getElementById(
        "decision"
    ).innerText =
        data.decision || "---";


    document.getElementById(
        "actionType"
    ).innerText =
        data.action_type || "---";


    // -------------------------------
    // HARDWARE
    // -------------------------------

    document.getElementById(
        "hardwareCommand"
    ).innerText =
        data.hardware_command ??
        "---";


    document.getElementById(
        "executedAction"
    ).innerText =
        data.executed_action ||
        "---";


    // -------------------------------
    // SAFETY
    // -------------------------------

    document.getElementById(
        "safetyStatus"
    ).innerText =
        data.safety_status ||
        "WAITING";


    document.getElementById(
        "safetyReason"
    ).innerText =
        data.safety_reason ||
        "---";


    // -------------------------------
    // VERIFICATION
    // -------------------------------

    document.getElementById(
        "verificationStatus"
    ).innerText =
        data.verification_status ||
        "---";


    document.getElementById(
        "verificationMessage"
    ).innerText =
        data.verification_message ||
        "---";


    // -------------------------------
    // ALERT
    // -------------------------------

    const alertElement =
        document.getElementById(
            "alert"
        );


    if (data.alert) {

        alertElement.innerText =
            "🚨 " + data.alert;

    } else {

        alertElement.innerText =
            "No active alerts.";

    }


    // -------------------------------
    // FINAL RESPONSE
    // -------------------------------

    document.getElementById(
        "response"
    ).innerText =
        data.response ||
        "---";


    // -------------------------------
    // RAW API DATA
    // -------------------------------

    document.getElementById(
        "rawJson"
    ).innerText =
        JSON.stringify(
            data,
            null,
            2
        );


    // -------------------------------
    // NOTIFICATION
    // -------------------------------

    handleNotification(data);

}


// =====================================
// NOTIFICATIONS
// =====================================

function handleNotification(data) {

    if (!data.alert) {

        previousAlert = null;

        return;

    }


    if (
        data.alert !== previousAlert
    ) {

        sendNotification(
            "ROBOAI Alert",
            data.alert
        );

        previousAlert =
            data.alert;

    }

}


// =====================================
// BROWSER NOTIFICATION
// =====================================

function sendNotification(
    title,
    message
) {

    if (
        "Notification" in window &&
        Notification.permission ===
        "granted"
    ) {

        new Notification(
            title,
            {
                body: message
            }
        );

    }

}


// =====================================
// ENABLE NOTIFICATIONS
// =====================================

const notificationBtn =
    document.getElementById(
        "notificationBtn"
    );


if (notificationBtn) {

    notificationBtn.addEventListener(
        "click",
        async () => {

            if (
                !("Notification" in window)
            ) {

                alert(
                    "Browser notifications are not supported."
                );

                return;

            }


            const permission =
                await Notification.requestPermission();


            if (
                permission ===
                "granted"
            ) {

                alert(
                    "Notifications enabled."
                );

            }

        }
    );

}


// =====================================
// REFRESH
// =====================================

const refreshBtn =
    document.getElementById(
        "refreshBtn"
    );


if (refreshBtn) {

    refreshBtn.addEventListener(
        "click",
        fetchFarmStatus
    );

}


// =====================================
// CLEAR
// =====================================

const clearBtn =
    document.getElementById(
        "clearBtn"
    );


if (clearBtn) {

    clearBtn.addEventListener(
        "click",
        () => {

            document.getElementById(
                "observation"
            ).innerText =
                "Waiting for sensor data...";


            document.getElementById(
                "decision"
            ).innerText =
                "---";


            document.getElementById(
                "actionType"
            ).innerText =
                "---";


            document.getElementById(
                "hardwareCommand"
            ).innerText =
                "---";


            document.getElementById(
                "executedAction"
            ).innerText =
                "---";


            document.getElementById(
                "safetyStatus"
            ).innerText =
                "WAITING";


            document.getElementById(
                "safetyReason"
            ).innerText =
                "---";


            document.getElementById(
                "verificationStatus"
            ).innerText =
                "---";


            document.getElementById(
                "verificationMessage"
            ).innerText =
                "---";


            document.getElementById(
                "alert"
            ).innerText =
                "No active alerts.";


            document.getElementById(
                "response"
            ).innerText =
                "Waiting for graph execution...";


            document.getElementById(
                "rawJson"
            ).innerText =
                "{}";

        }

    );

}


// =====================================
// AUTOMATIC POLLING
// =====================================

// Get latest farm data immediately

fetchFarmStatus();


// Then check every 3 seconds

setInterval(
    fetchFarmStatus,
    3000
);


// =====================================
// SAVE FARM PROFILE
// =====================================
// =====================================
// SAVE FARM PROFILE
// =====================================

const saveFarmBtn =
    document.getElementById("saveFarmBtn");

if (saveFarmBtn) {

    saveFarmBtn.addEventListener(
        "click",
        async () => {

            const crop =
                document.getElementById("farmCrop").value.trim();

            const cropStage =
                document.getElementById("farmCropStage").value.trim();

            const soilType =
                document.getElementById("farmSoilType").value.trim();

            const area =
                document.getElementById("farmArea").value.trim();


            if (!crop || !cropStage || !soilType || !area) {

                document.getElementById(
                    "farmSetupMessage"
                ).textContent =
                    "Please fill in all farm details.";

                return;
            }


            const farmData = {
                crop: crop,
                crop_stage: cropStage,
                soil_type: soilType,
                area: area
            };


            try {

                const response = await fetch(
                    "/farm-setup",
                    {
                        method: "POST",

                        headers: {
                            "Content-Type": "application/json"
                        },

                        body: JSON.stringify(farmData)
                    }
                );


                const data = await response.json();


                if (!response.ok) {

                    throw new Error(
                        data.detail ||
                        "Failed to save farm profile."
                    );
                }


                document.getElementById(
                    "farmSetupMessage"
                ).textContent =
                    "Farm profile saved successfully.";


                console.log(
                    "Farm profile saved:",
                    data.farm_profile
                );


            } catch (error) {

                console.error(
                    "Farm setup error:",
                    error
                );

                document.getElementById(
                    "farmSetupMessage"
                ).textContent =
                    "Failed to save farm profile.";

            }

        }
    );
}