import os
import subprocess
import getpass

# Variables de configuración
audit_checks = {
    "weak_passwords": True,
    "open_ports": True,
    "firewall_status": True,
    # Se pueden gregar más comprobaciones según sea necesario :D
}

def check_weak_passwords():
    if audit_checks["weak_passwords"]:
        
        # verificación de contraseñas débiles aquí
        pass  #reemplazar 'pass' con la lógica real

def check_open_ports():
    if audit_checks["open_ports"]:
        open_ports = subprocess.check_output(["netstat", "-an"]).decode("utf-8")
        # verificación de puertos abiertos aquí
        pass  # reemplazar 'pass' con la lógica real

def check_firewall():
    if audit_checks["firewall_status"]:
        # verificación del estado del firewall aquí
        pass  #reemplazar 'pass' con la lógica real

def run_security_audit():
    print("Realizando auditoría de seguridad...")
    check_weak_passwords()
    check_open_ports()
    check_firewall()
    print("Auditoría de seguridad completa.")

def configure_audit_checks():
    print("Configuración de auditoría de seguridad:")
    for check, status in audit_checks.items():
        response = input(f"¿Verificar {check.replace('_', ' ')}? (Sí/No, actual: {'Sí' if status else 'No'}): ").lower()
        audit_checks[check] = response.startswith("s")

def interactive_security_audit():
    configure_audit_checks()
    run_security_audit()

interactive_security_audit()
