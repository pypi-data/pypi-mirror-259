# MSPS - Maven Settings Profile S+witcher

MSPS is a simple tool to switch between different Maven settings profiles.

## Installation

```bash
pip install ...
```

## Usage examples

### Change profile without specifying a profile name

The next profile in the list of available profiles will be used.

```bash
msps switch
```
```plain
╭──────────── Maven Settings Profile Switcher ────────────╮
│                                                         │
│  Profile changed from current_profile to next_profile.  │
│                                                         │
╰─────────────────────────────────────────────────────────╯
```

### Change profile to a specific profile

The specified profile will be used.

```bash
msps switch work
```
```plain
╭───────────── Maven Settings Profile Switcher ──────────────╮
│                                                            │
│  M2_HOME: /home/testuser/.m2/                              │
│  Available settings profiles:                              │
│    - personal (/home/testuser/.m2/settings__personal.xml)  │
│    - work (/home/testuser/.m2/settings__work.xml)          │
│  Profile changed from personal to work.            │
│                                                            │
╰────────────────────────────────────────────────────────────╯
```

### Change profile to a specific profile that does not exist

The specified profile does not exist, so no changes will be made.

```bash
msps switch target_profile
```
```plain
╭───────────── Maven Settings Profile Switcher ──────────────╮
│                                                            │
│  Missing profile: target_profile                           │
│                                                            │
│  M2_HOME: /home/testuser/.m2/                              │
│  Available settings profiles:                              │
│    - personal (/home/testuser/.m2/settings__personal.xml)  │
│    - work (/home/testuser/.m2/settings__work.xml)          │
│  No changes were made.                                     │
│                                                            │
╰────────────────────────────────────────────────────────────╯
```

### List available profiles

```bash
msps list
```
```plain
╭───────────── Maven Settings Profile Switcher ──────────────╮
│                                                            │
│  Available settings profiles:                              │
│    - personal (/home/testuser/.m2/settings__personal.xml)  │
│    - work (/home/testuser/.m2/settings__work.xml)          │
│                                                            │
╰────────────────────────────────────────────────────────────╯
```