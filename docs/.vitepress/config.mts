import { defineConfig } from 'vitepress'

export default defineConfig({
  title: "Publishing Services",
  description: "Permissions Seeking System Documentation",

  head: [
    ['link', { rel: 'icon', type: 'image/svg+xml', href: '/logo.svg' }]
  ],

  themeConfig: {
    logo: '/logo.svg',

    nav: [
      { text: 'Home', link: '/' },
      { text: 'Overview', link: '/overview/' },
      { text: 'Workflows', link: '/workflows/' },
      { text: 'Systems', link: '/systems/' },
      { text: 'Reference', link: '/reference/' },
      { text: 'AI Agent Playbook', link: '/ai-agent-playbook/' }
    ],

    sidebar: {
      '/overview/': [
        {
          text: 'Overview',
          items: [
            { text: 'Introduction', link: '/overview/' },
            { text: 'Business Context', link: '/overview/business-context' },
            { text: 'Core Processes', link: '/overview/core-processes' },
            { text: 'Organization Structure', link: '/overview/organization' },
            { text: 'Key Stakeholders', link: '/overview/stakeholders' }
          ]
        }
      ],
      '/workflows/': [
        {
          text: 'Workflows',
          items: [
            { text: 'Process Overview', link: '/workflows/' },
            { text: 'Tier-Based Model', link: '/workflows/tier-model' },
            { text: 'Health Sciences (HS)', link: '/workflows/health-sciences' },
            { text: 'Science & Technology (S&T)', link: '/workflows/science-technology' },
            { text: 'Mode of Contact', link: '/workflows/mode-of-contact' },
            { text: 'Follow-up & Escalation', link: '/workflows/followup-escalation' }
          ]
        }
      ],
      '/systems/': [
        {
          text: 'Systems & Tools',
          items: [
            { text: 'Systems Overview', link: '/systems/' },
            { text: 'RPC System', link: '/systems/rpc' },
            { text: 'EMSS', link: '/systems/emss' },
            { text: 'ELSA', link: '/systems/elsa' },
            { text: 'Editorial System', link: '/systems/editorial-system' },
            { text: 'CCC RightsLink', link: '/systems/ccc-rightslink' },
            { text: 'External Resources', link: '/systems/external-resources' }
          ]
        }
      ],
      '/reference/': [
        {
          text: 'Reference',
          items: [
            { text: 'Data Dictionary', link: '/reference/' },
            { text: 'Email Templates', link: '/reference/email-templates' },
            { text: 'Permission Log Excel', link: '/reference/permission-log-excel' },
            { text: 'File Naming Conventions', link: '/reference/file-naming' },
            { text: 'STM Guidelines', link: '/reference/stm-guidelines' },
            { text: 'Glossary', link: '/reference/glossary' }
          ]
        }
      ],
      '/ai-agent-playbook/': [
        {
          text: 'AI Agent Playbook',
          items: [
            { text: 'Overview', link: '/ai-agent-playbook/' },
            { text: 'Triggers Overview', link: '/ai-agent-playbook/triggers' },
            { text: 'Agentic Flow Runbook', link: '/ai-agent-playbook/agentic-flow-runbook' }
          ]
        },
        {
          text: 'Flows',
          items: [
            { text: 'Flow 01 - Intake and Sync', link: '/ai-agent-playbook/flows/01-intake-sync' },
            { text: 'Flow 02 - Inventory and Log Processing', link: '/ai-agent-playbook/flows/02-inventory-log-processing' },
            { text: 'Flow 03 - Research and Classification', link: '/ai-agent-playbook/flows/03-research-classification' },
            { text: 'Flow 04 - Permission Request Execution', link: '/ai-agent-playbook/flows/04-permission-request-execution' },
            { text: 'Flow 05 - Follow-Up and Escalation', link: '/ai-agent-playbook/flows/05-followup-escalation' },
            { text: 'Flow 06 - Response Handling', link: '/ai-agent-playbook/flows/06-response-handling' },
            { text: 'Flow 07 - Fees and Approvals', link: '/ai-agent-playbook/flows/07-fees-approvals' },
            { text: 'Flow 08 - Evidence and Reporting', link: '/ai-agent-playbook/flows/08-evidence-reporting' },
            { text: 'Flow 09 - Project Closure', link: '/ai-agent-playbook/flows/09-project-closure' },
            { text: 'Flow 10 - Audit and Observability', link: '/ai-agent-playbook/flows/10-audit-observability' },
            { text: 'Flow 11 - Sync Retry and Failure Recovery', link: '/ai-agent-playbook/flows/11-sync-retry-recovery' }
          ]
        },
        {
          text: 'Tier Flows',
          items: [
            { text: 'HS Tier 4 - Full Service', link: '/ai-agent-playbook/flows/hs-tier-4' },
            { text: 'HS Tier 0 - Validation Only', link: '/ai-agent-playbook/flows/hs-tier-0' },
            { text: 'HS Rule of 10', link: '/ai-agent-playbook/flows/hs-rule-of-10' },
            { text: 'S&T Tier 1 - Author Obtains', link: '/ai-agent-playbook/flows/st-tier-1' },
            { text: 'S&T Tier 2 - Author Log, AI Seeks', link: '/ai-agent-playbook/flows/st-tier-2' },
            { text: 'S&T Tier 3 - Full Service', link: '/ai-agent-playbook/flows/st-tier-3' }
          ]
        },
        {
          text: 'Agents',
          items: [
            { text: 'Coordinator Agent', link: '/ai-agent-playbook/agents/coordinator' },
            { text: 'Intake and Sync Agent', link: '/ai-agent-playbook/agents/intake-sync' },
            { text: 'Inventory and Log Agent', link: '/ai-agent-playbook/agents/inventory-log' },
            { text: 'Research and Classification Agent', link: '/ai-agent-playbook/agents/research-classification' },
            { text: 'Outreach and Response Agent', link: '/ai-agent-playbook/agents/outreach-response' },
            { text: 'Finance and Approval Agent', link: '/ai-agent-playbook/agents/finance-approval' },
            { text: 'Evidence and Reporting Agent', link: '/ai-agent-playbook/agents/evidence-reporting' }
          ]
        }
      ]
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/elsevier' }
    ],

    search: {
      provider: 'local'
    },

    footer: {
      message: 'Publishing Services Documentation',
      copyright: 'Copyright Ampcome - www.ampcome.com'
    }
  }
})
