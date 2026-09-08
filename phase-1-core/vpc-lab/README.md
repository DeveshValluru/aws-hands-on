# Lab 3 — VPC (Virtual Private Cloud)

**Goal:** understand AWS networking by exploring the **default VPC** your EC2 instance
lived in — VPC, subnets, route tables, internet gateway, security groups — all read-only
(free). Then optionally build a minimal custom VPC to see the pieces assembled.

## Mental model
- **A VPC is your own private, isolated network inside AWS** — your own slice of IP space where your resources live and talk to each other.
- Every account gets a **default VPC** per region so things "just work" (your EC2 instance used it automatically).
- The pieces:
  | Piece | What it is | Analogy |
  |---|---|---|
  | **VPC** | the whole private network + its IP range (CIDR) | a gated campus |
  | **CIDR block** | the IP range, e.g. `172.31.0.0/16` | the campus's street-address range |
  | **Subnet** | a slice of the VPC, lives in ONE Availability Zone | a building on campus |
  | **Route table** | rules: "traffic to X goes to Y" | the campus road map |
  | **Internet Gateway (IGW)** | the door to the public internet | the campus main gate |
  | **NAT Gateway** | lets private subnets reach OUT (but stay unreachable) — ⚠️ costs money | a one-way service exit |
  | **Security Group** | firewall on an instance (stateful) | a lock on each building door |
  | **NACL** | firewall on a subnet (stateless) | a checkpoint at each building entrance |

## Public vs private subnet — the key distinction
- **Public subnet** = its route table has a route to an **Internet Gateway** → resources can be reached from / reach the internet.
- **Private subnet** = no IGW route → isolated; reaches out only via a **NAT Gateway** (e.g. databases, internal services).

## Cost note
Exploring (describe-*) is free. VPCs, subnets, route tables, and internet gateways are
**free**. The ONLY things that cost money: **NAT Gateways** and **Elastic IPs**. We avoid both.
