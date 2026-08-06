# -*- coding: utf-8 -*-
"""
Line icon set: one distinct mark per division, capability, solution and service.

All icons are drawn on a 24x24 grid with a 1.5 stroke in currentColor, so they
inherit text colour and work on paper, bone and ink without variants. Inline SVG
rather than a sprite or an icon font: nothing extra to download, and at ~180
bytes each the cost is far below a network request.
"""

_P = {}

# ------------------------------ DIVISIONS ------------------------------
_P["healthcare"] = '<path d="M3.5 12h3.2l1.8-4.5 3 9 2.2-5.5 1.6 3h5.2"/>'  # pulse trace
_P["trades"] = ('<path d="M14.7 6.3a3.9 3.9 0 0 0 5 5L15 16.6l-3.2 3.2a2 2 0 0 1-2.8-2.8l3.2-3.2Z"/>'
                '<path d="M9.2 14.8 4.6 10.2a3.9 3.9 0 0 1 5-5"/>')  # wrench
_P["dtc"] = ('<path d="M3.6 7.6 12 3.5l8.4 4.1v8.8L12 20.5l-8.4-4.1Z"/>'
             '<path d="M3.6 7.6 12 11.8l8.4-4.2M12 11.8v8.7"/>')  # parcel
_P["professional-services"] = ('<rect x="3" y="7.2" width="18" height="12.4" rx="1.6"/>'
                               '<path d="M8.6 7.2V5.8a1.8 1.8 0 0 1 1.8-1.8h3.2a1.8 1.8 0 0 1 1.8 1.8v1.4"/>'
                               '<path d="M3 12.4h18"/>')  # briefcase

# ------------------------------ CAPABILITIES ------------------------------
_P["paid-media"] = ('<circle cx="12" cy="12" r="8.2"/><circle cx="12" cy="12" r="4.2"/>'
                    '<circle cx="12" cy="12" r=".9" fill="currentColor" stroke="none"/>')
_P["performance-creative"] = ('<rect x="3.2" y="5.4" width="17.6" height="13.2" rx="1.8"/>'
                              '<path d="M3.2 9.4h17.6M7.6 5.4v4M16.4 5.4v4"/>'
                              '<path d="M10.6 12.6v3.4l3-1.7Z"/>')
_P["seo-ai-search"] = ('<circle cx="10.6" cy="10.6" r="6.4"/><path d="M15.4 15.4 20.5 20.5"/>'
                       '<path d="M10.6 7.6l.9 2.1 2.1.9-2.1.9-.9 2.1-.9-2.1-2.1-.9 2.1-.9Z"/>')
_P["content-authority"] = ('<path d="M6 3.6h8.4L19 8.2v12.2H6Z"/><path d="M14.2 3.6v4.8H19"/>'
                           '<path d="M9 12.4h7M9 15.8h7"/>')
_P["websites-cro"] = ('<rect x="3" y="4.6" width="18" height="14.8" rx="1.8"/>'
                      '<path d="M3 8.8h18"/><circle cx="6.2" cy="6.7" r=".7" fill="currentColor" stroke="none"/>'
                      '<path d="M8.8 15.6l2.6-2.6 2 2 3-3.2"/>')
_P["crm-automation"] = ('<circle cx="6" cy="6.4" r="2.6"/><circle cx="18" cy="12" r="2.6"/>'
                        '<circle cx="6" cy="17.6" r="2.6"/><path d="M8.4 7.6 15.6 11M15.6 13 8.4 16.4"/>')
_P["analytics-intelligence"] = ('<path d="M3.6 20.4h16.8"/><path d="M7 20.4v-6.2M12 20.4V7.6M17 20.4v-9.4"/>')

# ------------------------------ SOLUTIONS ------------------------------
_P["multi-location-growth"] = ('<path d="M7 10.4c0 3.4 4 8.4 4 8.4s4-5 4-8.4a4 4 0 1 0-8 0Z"/>'
                               '<circle cx="11" cy="10.2" r="1.5"/><path d="M17.4 14.6c1.4 1.7 2.2 3.2 2.2 3.2"/>')
_P["market-expansion"] = ('<circle cx="12" cy="12" r="8.4"/><path d="M3.6 12h16.8"/>'
                          '<path d="M12 3.6a13 13 0 0 1 0 16.8a13 13 0 0 1 0-16.8Z"/>')
_P["new-location-launch"] = ('<path d="M12 3.4c3 2.2 4.6 5.4 4.6 9.2L12 17.4l-4.6-4.8c0-3.8 1.6-7 4.6-9.2Z"/>'
                             '<circle cx="12" cy="10.6" r="1.7"/><path d="M9.4 18.2 8 21.2M14.6 18.2 16 21.2"/>')
_P["lead-conversion"] = ('<path d="M3.4 6.2h17.2l-6.6 7.6v5.4l-4 1.6v-7Z"/>')
_P["sales-enablement"] = ('<path d="M4 18.4V8.6l8-4.8 8 4.8v9.8"/><path d="M9 18.4v-5h6v5"/>'
                          '<path d="M3 18.4h18"/>')
_P["marketing-attribution"] = ('<path d="M3.6 20.4h16.8"/><path d="M6 16.6l4.2-5 3.4 2.8 4.6-6.4"/>'
                               '<circle cx="6" cy="16.6" r="1.2"/><circle cx="18.2" cy="8" r="1.2"/>')
_P["digital-transformation"] = ('<path d="M20 7.6A8.4 8.4 0 0 0 5 9.4"/><path d="M4 16.4A8.4 8.4 0 0 0 19 14.6"/>'
                                '<path d="M20 3.8v3.8h-3.8M4 20.2v-3.8h3.8"/>')
_P["talent-acquisition"] = ('<circle cx="10" cy="8.4" r="3.4"/>'
                            '<path d="M4 19.6c0-3.3 2.7-5.4 6-5.4s6 2.1 6 5.4"/>'
                            '<path d="M18.4 6.6v5.2M15.8 9.2H21"/>')

# ------------------------------ SERVICES ------------------------------
_P["digital-marketing"] = ('<rect x="3.4" y="3.4" width="7.2" height="7.2" rx="1.4"/>'
                           '<rect x="13.4" y="3.4" width="7.2" height="7.2" rx="1.4"/>'
                           '<rect x="3.4" y="13.4" width="7.2" height="7.2" rx="1.4"/>'
                           '<path d="M13.4 17h7.2M17 13.4v7.2"/>')
_P["performance-marketing"] = ('<path d="M4.6 19.4c-1-3.6 1.4-9.8 6.4-13 3-2 6.6-2.6 8.4-2.4.2 1.8-.4 5.4-2.4 8.4-3.2 5-9.4 7.4-13 6.4Z"/>'
                               '<circle cx="14.6" cy="9.4" r="1.8"/><path d="M4.6 19.4 8 16"/>')
_P["paid-search"] = ('<circle cx="10.4" cy="10.4" r="6.2"/><path d="M15 15 20.4 20.4"/>'
                     '<path d="M8.2 11.4h4.4M10.4 8.2v6.4"/>')
_P["google-ads"] = ('<path d="M5.6 4.6v13.2l3.6-3.2h8.4"/><path d="M9.6 8.4h6.4"/>'
                    '<path d="M17.6 14.6 21 21l-3.4-1.4L14.2 21Z"/>')
_P["paid-search-shopping"] = ('<path d="M3.8 6.4h2.6l2.2 9.6h9.2l1.8-6.8H7.2"/>'
                              '<circle cx="10.4" cy="19" r="1.4"/><circle cx="17" cy="19" r="1.4"/>')
_P["paid-social"] = ('<path d="M4 5.4h11.4a2 2 0 0 1 2 2v5.4a2 2 0 0 1-2 2H9l-5 3.4Z"/>'
                     '<path d="M8 9h5.4M8 11.6h3.4"/>')
_P["seo"] = ('<circle cx="10.4" cy="10.4" r="6.2"/><path d="M15 15 20.4 20.4"/>'
             '<path d="M7.8 12.2 9.8 9.6l1.8 1.6 2.6-3.2"/>')
_P["local-seo"] = ('<path d="M6.2 10.4c0 4.4 5.8 10.2 5.8 10.2s5.8-5.8 5.8-10.2a5.8 5.8 0 1 0-11.6 0Z"/>'
                   '<circle cx="12" cy="10.2" r="2.2"/>')
_P["ai-search"] = ('<path d="M12 3.4l1.9 4.7 4.7 1.9-4.7 1.9L12 16.6l-1.9-4.7-4.7-1.9 4.7-1.9Z"/>'
                   '<path d="M18.4 15.6l.9 2.1 2.1.9-2.1.9-.9 2.1-.9-2.1-2.1-.9 2.1-.9Z"/>')
_P["web-design"] = ('<rect x="3" y="4.6" width="18" height="14.8" rx="1.8"/><path d="M3 8.8h18"/>'
                    '<circle cx="6.2" cy="6.7" r=".7" fill="currentColor" stroke="none"/>'
                    '<path d="M7.4 12.2h4.2v4.6H7.4ZM14 12.2h2.8M14 15h2.8"/>')
_P["shopify-cro"] = ('<path d="M3.8 6.4h2.6l2.2 9.6h9.2l1.8-6.8H7.2"/>'
                     '<circle cx="10.4" cy="19" r="1.4"/><circle cx="17" cy="19" r="1.4"/>'
                     '<path d="M13.4 4.2v3.6M11.6 6h3.6"/>')
_P["crm-revops"] = ('<ellipse cx="12" cy="6.2" rx="7.4" ry="2.8"/>'
                    '<path d="M4.6 6.2v11.6c0 1.5 3.3 2.8 7.4 2.8s7.4-1.3 7.4-2.8V6.2"/>'
                    '<path d="M4.6 12c0 1.5 3.3 2.8 7.4 2.8s7.4-1.3 7.4-2.8"/>')
_P["email-sms"] = ('<rect x="3" y="5.4" width="18" height="13.2" rx="1.8"/>'
                   '<path d="M3.6 6.6 12 12.8l8.4-6.2"/>')
_P["content-marketing"] = ('<path d="M6 3.6h8.4L19 8.2v12.2H6Z"/><path d="M14.2 3.6v4.8H19"/>'
                           '<path d="M9 12.4h7M9 15.8h4.4"/>')
_P["thought-leadership"] = ('<path d="M8.4 5.4c-1.8 0-3.2 1.4-3.2 3.2s1.4 3.2 3.2 3.2c.4 0 .8-.1 1.1-.2-.3 2-1.6 3.6-3.3 4.4"/>'
                            '<path d="M17.4 5.4c-1.8 0-3.2 1.4-3.2 3.2s1.4 3.2 3.2 3.2c.4 0 .8-.1 1.1-.2-.3 2-1.6 3.6-3.3 4.4"/>')
_P["ad-creative"] = ('<path d="M3.4 8.4a2 2 0 0 1 2-2h2.2l1.4-2h6l1.4 2h2.2a2 2 0 0 1 2 2v9.2a2 2 0 0 1-2 2H5.4a2 2 0 0 1-2-2Z"/>'
                     '<circle cx="12" cy="12.6" r="3.4"/>')
_P["analytics"] = ('<rect x="3" y="4.6" width="18" height="14.8" rx="1.8"/>'
                   '<path d="M7 15.6v-3.2M11 15.6V9M15 15.6v-4.6"/>')
_P["call-tracking"] = ('<path d="M8 3.8 10.2 8l-2 1.8a11 11 0 0 0 5 5l1.8-2 4.2 2.2-1 3a2 2 0 0 1-2.2 1.2C10.6 18.4 5.6 13.4 4.6 7a2 2 0 0 1 1.2-2.2Z"/>')
_P["ecommerce-growth"] = ('<path d="M3.6 7.6 12 3.5l8.4 4.1v8.8L12 20.5l-8.4-4.1Z"/>'
                          '<path d="M3.6 7.6 12 11.8l8.4-4.2M12 11.8v8.7"/>'
                          '<path d="M15.6 6.4 19 3M19 3h-2.6M19 3v2.6"/>')
_P["marketplace-marketing"] = ('<path d="M4 9.4V19.4h16V9.4"/><path d="M3 9.4 5 4.6h14l2 4.8a2.6 2.6 0 0 1-4.5 0 2.6 2.6 0 0 1-4.5 0 2.6 2.6 0 0 1-4.5 0A2.6 2.6 0 0 1 3 9.4Z"/>'
                               '<path d="M9.8 19.4v-5h4.4v5"/>')


def icon(name, cls=""):
    """Inline SVG for a slug. Returns empty string for unknown names."""
    d = _P.get(name)
    if not d:
        return ""
    c = f' class="{cls}"' if cls else ""
    return (f'<svg{c} viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" '
            f'aria-hidden="true" focusable="false">{d}</svg>')


def has_icon(name):
    return name in _P


NAMES = sorted(_P)
