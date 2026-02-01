#!/usr/bin/env python3
"""
Process Permissions and Rights Demonstration Script
Lab03 - Process Management & Scheduling Analysis

This script demonstrates Linux process permissions, user rights, and security concepts.
It shows how different users and processes have different levels of access and privileges.
"""

import os
import sys
import subprocess
import time
import threading
from datetime import datetime

def get_current_user_info():
    """Get current user information and privileges"""
    print("=" * 60)
    print("🔍 CURRENT USER INFORMATION")
    print("=" * 60)
    
    # Get current user ID and group ID
    uid = os.getuid()
    gid = os.getgid()
    print(f"Current User ID (UID): {uid}")
    print(f"Current Group ID (GID): {gid}")
    
    # Get username
    try:
        import pwd
        user_info = pwd.getpwuid(uid)
        print(f"Username: {user_info.pw_name}")
        print(f"Home Directory: {user_info.pw_dir}")
        print(f"Shell: {user_info.pw_shell}")
    except ImportError:
        print("pwd module not available")
    
    # Check if running as root
    is_root = (uid == 0)
    print(f"Running as root: {'YES' if is_root else 'NO'}")
    
    # Get effective user ID
    euid = os.geteuid()
    print(f"Effective UID: {euid}")
    print(f"Effective GID: {os.getegid()}")
    
    return uid, gid, is_root

def demonstrate_process_creation():
    """Demonstrate process creation with different privileges"""
    print("\n" + "=" * 60)
    print("🚀 PROCESS CREATION DEMONSTRATION")
    print("=" * 60)
    
    # Show current process information
    pid = os.getpid()
    ppid = os.getppid()
    print(f"Current Process PID: {pid}")
    print(f"Parent Process PID: {ppid}")
    
    # Create a child process
    print("\nCreating child process...")
    child_pid = os.fork()
    
    if child_pid == 0:
        # Child process
        print(f"Child Process - PID: {os.getpid()}, Parent: {os.getppid()}")
        print(f"Child Process - UID: {os.getuid()}, GID: {os.getgid()}")
        
        # Simulate some work
        for i in range(3):
            print(f"Child working... {i+1}/3")
            time.sleep(1)
        
        print("Child process finished")
        sys.exit(0)
    else:
        # Parent process
        print(f"Parent Process - PID: {os.getpid()}")
        print(f"Child Process PID: {child_pid}")
        
        # Wait for child to complete
        os.wait()
        print("Parent: Child process completed")

def demonstrate_file_permissions():
    """Demonstrate file permissions and access rights"""
    print("\n" + "=" * 60)
    print("📁 FILE PERMISSIONS DEMONSTRATION")
    print("=" * 60)
    
    # Create a test file
    test_file = "permission_test.txt"
    
    try:
        # Create file with current user permissions
        with open(test_file, 'w') as f:
            f.write("This is a test file for permission demonstration\n")
            f.write(f"Created by UID: {os.getuid()}\n")
            f.write(f"Created at: {datetime.now()}\n")
        
        print(f"Created test file: {test_file}")
        
        # Check file permissions
        stat_info = os.stat(test_file)
        print(f"File permissions (octal): {oct(stat_info.st_mode)[-3:]}")
        print(f"File owner UID: {stat_info.st_uid}")
        print(f"File group GID: {stat_info.st_gid}")
        
        # Try to read the file
        try:
            with open(test_file, 'r') as f:
                content = f.read()
                print("✅ Successfully read the file")
                print("File content preview:")
                print(content[:100] + "..." if len(content) > 100 else content)
        except PermissionError:
            print("❌ Permission denied to read file")
        
        # Try to modify file permissions
        try:
            os.chmod(test_file, 0o600)  # Read/write for owner only
            print("✅ Successfully changed file permissions to 600")
        except PermissionError:
            print("❌ Permission denied to change file permissions")
        
        # Clean up
        os.remove(test_file)
        print("✅ Test file cleaned up")
        
    except Exception as e:
        print(f"❌ Error in file permissions demo: {e}")

def demonstrate_system_commands():
    """Demonstrate system commands with different privilege levels"""
    print("\n" + "=" * 60)
    print("⚙️ SYSTEM COMMANDS DEMONSTRATION")
    print("=" * 60)
    
    commands_to_test = [
        ("whoami", "Show current username"),
        ("id", "Show user and group IDs"),
        ("ps -u $USER", "Show current user's processes"),
        ("ls -la /proc/self", "Show current process information"),
        ("cat /proc/self/status", "Show detailed process status"),
    ]
    
    for cmd, description in commands_to_test:
        print(f"\n🔧 {description}")
        print(f"Command: {cmd}")
        print("-" * 40)
        
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                print("✅ Command executed successfully:")
                print(result.stdout[:200] + "..." if len(result.stdout) > 200 else result.stdout)
            else:
                print(f"❌ Command failed with return code {result.returncode}")
                print(f"Error: {result.stderr}")
        except subprocess.TimeoutExpired:
            print("⏰ Command timed out")
        except Exception as e:
            print(f"❌ Error executing command: {e}")

def demonstrate_privilege_escalation():
    """Demonstrate privilege escalation concepts"""
    print("\n" + "=" * 60)
    print("🔐 PRIVILEGE ESCALATION DEMONSTRATION")
    print("=" * 60)
    
    # Check if we can use sudo
    try:
        result = subprocess.run("sudo -n true", shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Sudo access available (no password required)")
        else:
            print("⚠️ Sudo access requires password or not available")
    except Exception as e:
        print(f"❌ Error checking sudo access: {e}")
    
    # Show current capabilities
    try:
        with open('/proc/self/status', 'r') as f:
            status_content = f.read()
            if 'CapInh:' in status_content:
                print("\n📋 Process Capabilities:")
                for line in status_content.split('\n'):
                    if line.startswith('Cap'):
                        print(f"  {line}")
    except Exception as e:
        print(f"❌ Error reading process capabilities: {e}")
    
    # Show process limits
    try:
        with open('/proc/self/limits', 'r') as f:
            limits = f.read()
            print("\n📊 Process Resource Limits:")
            print(limits[:300] + "..." if len(limits) > 300 else limits)
    except Exception as e:
        print(f"❌ Error reading process limits: {e}")

def monitor_process_changes():
    """Monitor process changes in real-time"""
    print("\n" + "=" * 60)
    print("👀 PROCESS MONITORING DEMONSTRATION")
    print("=" * 60)
    
    print("Starting process monitoring for 60 seconds...")
    print("Watch for new processes being created...")
    
    # Get initial process list
    try:
        result = subprocess.run("ps -eo pid,comm | wc -l", shell=True, capture_output=True, text=True)
        initial_count = int(result.stdout.strip()) if result.returncode == 0 else 0
        print(f"Initial process count: {initial_count}")
    except:
        initial_count = 0
    
    # Monitor for 10 seconds
    start_time = time.time()
    while time.time() - start_time < 60:
        try:
            # Show current user processes
            result = subprocess.run("ps -u $USER -o pid,comm,pcpu,pmem", shell=True, 
                                  capture_output=True, text=True, timeout=2)
            if result.returncode == 0:
                lines = result.stdout.strip().split('\n')
                if len(lines) > 1:  # More than just header
                    print(f"\n📊 Current user processes ({len(lines)-1} total):")
                    for line in lines[:6]:  # Show first 5 processes
                        print(f"  {line}")
                    if len(lines) > 6:
                        print(f"  ... and {len(lines)-6} more processes")
        except:
            pass
        
        time.sleep(2)
    
    print("\n✅ Process monitoring completed")

def main():
    """Main function to run all demonstrations"""
    print("🔐 Linux Process Permissions and Rights Demonstration")
    print("=" * 60)
    print(f"Started at: {datetime.now()}")
    print(f"Python version: {sys.version}")
    print(f"Script PID: {os.getpid()}")
    
    try:
        # Run all demonstrations
        get_current_user_info()
        demonstrate_process_creation()
        demonstrate_file_permissions()
        demonstrate_system_commands()
        demonstrate_privilege_escalation()
        monitor_process_changes()
        
        print("\n" + "=" * 60)
        print("✅ ALL DEMONSTRATIONS COMPLETED")
        print("=" * 60)
        print("Key Learning Points:")
        print("1. Process permissions are inherited from parent processes")
        print("2. File access is controlled by ownership and permissions")
        print("3. System commands show different information based on privileges")
        print("4. Privilege escalation requires proper authentication")
        print("5. Process monitoring helps understand system behavior")
        
    except KeyboardInterrupt:
        print("\n🛑 Demonstration interrupted by user")
    except Exception as e:
        print(f"\n❌ Error during demonstration: {e}")
    finally:
        print(f"\nFinished at: {datetime.now()}")

if __name__ == "__main__":
    main()
