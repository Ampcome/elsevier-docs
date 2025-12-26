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
      { text: 'Reference', link: '/reference/' }
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
      copyright: 'Elsevier'
    }
  }
})
