[app]
title = IndominusApp
package.name = indominusapp
package.domain = org.indominus


source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,java

version = 1.0.0

requirements = python3,kivy==2.3.0,https://github.com/kivymd/KivyMD/archive/master.zip,pillow,materialyoucolor,asyncgui,asynckivy

# Java/Kotlin adicionales del proyecto (FCM receiver, Notification
# Listener). Buildozer los copia dentro de src/main/java al compilar.
android.add_src = ./java_src

# --- Permisos ---
# CALL_PHONE: hacer llamadas (Intent.ACTION_CALL)
# ACCESS_FINE_LOCATION / ACCESS_COARSE_LOCATION: GPS
# MODIFY_AUDIO_SETTINGS: control de volumen del "buscador de teléfono"
# POST_NOTIFICATIONS: requerido desde Android 13 para que la propia app
#   pueda usar notificaciones locales (no confundir con el listener)
# INTERNET / ACCESS_NETWORK_STATE: llamadas a Firebase/API Gateway
# FOREGROUND_SERVICE: mantener vivo el proceso que escucha FCM
# RECEIVE_BOOT_COMPLETED: re-registrar el listener tras reiniciar el móvil
# BIND_NOTIFICATION_LISTENER_SERVICE: requerido por el propio sistema
#   para el NotificationListenerService (se declara aquí Y en el
#   AndroidManifest via android.manifestPlaceholders más abajo)
android.permissions = CALL_PHONE,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,MODIFY_AUDIO_SETTINGS,POST_NOTIFICATIONS,INTERNET,ACCESS_NETWORK_STATE,FOREGROUND_SERVICE,RECEIVE_BOOT_COMPLETED

android.api = 34
android.minapi = 26
android.ndk = 25b
android.archs = arm64-v8a,armeabi-v7a

# Google Play Services (necesario para Firebase Cloud Messaging)
android.gradle_dependencies = com.google.firebase:firebase-analytics:21.5.0, com.google.firebase:firebase-firestore:24.10.0, com.google.firebase:firebase-messaging:23.4.0

# google-services.json (descargado de la consola Firebase) debe copiarse
# a la raíz del proyecto Android generado; ver instrucciones de
# despliegue para el paso exacto con Buildozer.
android.add_google_services_json = google-services.json

# Necesario para que Gradle aplique el plugin de Google Services
android.gradle_plugins = com.google.gms:google-services:4.4.2

orientation = portrait
fullscreen = 0

icon.filename = %(source.dir)s/data/icon.png
presplash.filename = %(source.dir)s/data/presplash.png

[buildozer]
log_level = 2
warn_on_root = 1
