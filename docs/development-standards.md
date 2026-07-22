# Development Standards

## Purpose

This document defines the engineering standards for every project generated from this template.

The goal is consistency, maintainability, readability, and predictable quality across all repositories.

---

# Core Principles

## Correctness before optimization

Code must be correct before it is optimized.

Performance optimizations require evidence (profiling, benchmarks, or measurable impact).

---

## Simplicity

Choose the simplest solution that:

* solves the problem
* is maintainable
* scales reasonably

Avoid unnecessary abstraction.

---

## Readability

Code is written for humans first.

Prefer:

* descriptive names
* small functions
* explicit behavior
* minimal nesting

---

## Single Responsibility

Functions, modules, and classes should have one clear responsibility.

---

## Explicit over implicit

Avoid hidden behavior.

Configuration, dependencies, and side effects should be obvious.

---

# Python Standards

* Use modern Python features where appropriate.
* Prefer type hints for public functions.
* Avoid global mutable state.
* Use dataclasses or Pydantic models where appropriate.
* Raise specific exceptions.

---

# Project Structure

Generated projects follow the `src` layout.

Tests never import from the repository root.

---

# Dependency Management

* Use `uv`.
* Commit the lockfile.
* Remove unused dependencies promptly.
* Prefer well-maintained libraries with strong documentation.

---

# Configuration

Configuration must:

* come from environment variables
* be validated during startup
* never contain secrets in Git

`.env.example` documents required variables.

---

# Logging

Applications should:

* use structured, informative logging
* avoid logging secrets
* log errors with useful context
* avoid excessive debug output in production

---

# Testing

Every new feature should include tests where practical.

Tests should be:

* deterministic
* isolated
* fast
* readable

---

# Git

Commits should:

* represent one logical change
* have clear commit messages
* pass local quality checks before being committed

Never commit:

* secrets
* credentials
* generated artifacts
* virtual environments
* local editor files

---

# Documentation

Every meaningful architectural decision should be documented.

README files should explain:

* purpose
* installation
* usage
* development workflow

---

# Continuous Integration

The CI pipeline is the authoritative quality gate.

Code should not be merged unless CI succeeds.

---

# Security

Use secure defaults.

Validate external input.

Pin dependencies where appropriate.

Never expose secrets in source code, logs, or container images.

---

# Continuous Improvement

Standards may evolve.

Changes should be intentional, documented, and recorded through an Architecture Decision Record (ADR).
